#!/usr/bin/env python2

# Copyright (c) 2017 Santiago Murcia Cadavid
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

__author__ = 'cadavidmurcia@gmail.com'

import json
import re

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from bs4 import BeautifulSoup, NavigableString
from .CustomException import ElementDoesNotExistAssertionError, ElementExistsAssertionError
from .LinkVerifier import LinkVerifier
import Base.CustomExpectedConditions as CEC
import Base.Config as Config

def build_prod_url_table():
  """
  Build a table from site keys to the base prod URL for each site.
  """

  for device in ['Desktop', 'Mobile']:
    # The prod URLs would be correct for the mobile site, but they will resolve
    # only to desktop sites without a mobile User-Agent header. To avoid wrong
    # behavior, leave mobile site keys out of the table.

    for page in ['PageOne', 'PageTwo', 'PageThree', 'PageFour',
                    'PageFive', 'PageSix', 'PageSeven']:
      url = 'http://somethinghere.com/{0}/'.format(page.lower())
      yield (device + page, url)
    yield (device + 'PlosCollections', 'http://collections.plos.org/')

    #Review Original File

PROD_URL_TABLE = dict(build_prod_url_table())

class PomPage(object):
  """
  Model an abstract base Journal page.
  """

  PROD_URL = ''

  def __init__(self, driver, urlSuffix=''):

    # Internal WebDriver-related protected members
    self._driver = driver
    self._wait = WebDriverWait(self._driver, Config.wait_timeout)
    self._actions = ActionChains(self._driver)

    base_url = self.__buildEnvironmentURL(urlSuffix)

    # Prevents WebDriver from navigating to a page more than once (there should be only one starting point for a test)
    if not hasattr(self._driver, 'navigated'):
      try:
        self._driver.get(base_url)
        self._driver.navigated = True
      except TimeoutException as toe:
        print ('\t[WebDriver Error] WebDriver timed out while trying to load the requested web page "%s".' % base_url)
        raise toe

    # Internal private member
    self.__linkVerifier = LinkVerifier()

    # Locators - Instance variables unique to each instance
    self._article_type_menu = (By.ID, 'article-type-menu')
    self._page_body = (By.TAG_NAME, 'body')

  # POM Actions
  def __buildEnvironmentURL(self, urlSuffix):
    """
    *Private* method to detect on which environment we are running the test.
    Then builds up a URL accordingly

    1. urlSuffix: String representing the suffix to append to the URL. It is generally provided by

    **Returns** A string representing the whole URL from where our test starts
    """

    journalName = str(self)
    env = Config.environment.lower()
    if env == 'prod':
      base_url = self._translate_to_prod_url(urlSuffix) or self.PROD_URL
    elif 'Collections' in journalName:
      base_url = Config.collections_url + urlSuffix
    else:
      base_url = Config.base_url + urlSuffix
    return base_url

  def _translate_to_prod_url(self, dev_path):
    """
    Translate a dev-box path to a production URL.

    Example:
      '/DesktopPlosBiology/article?id=10.1371/journal.pbio.1001199'
    to
      'http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001199'

    Returns None if the path does not start with a token that matches a
    site key.
    """

    match = re.match(r'/(.*?)/(.*)', dev_path)
    if match:
      site_key, url_suffix = match.groups()
      if site_key in PROD_URL_TABLE:
        base_url = PROD_URL_TABLE[site_key]
        return base_url + url_suffix
    return None

  def _get(self, locator):
    try:
      return self._wait.until(EC.visibility_of_element_located(locator)).wrapped_element
    except TimeoutException:
      print ('\t[WebDriver Error] WebDriver timed out while trying to identify element by %s.' % str(locator))
      raise ElementDoesNotExistAssertionError(locator)

  def _check_for_invisible_element(self, locator):
    try:
      return self._wait.until(EC.invisibility_of_element_located(locator)).wrapped_element
    except TimeoutException:
      print ('\t[WebDriver Error] WebDriver timed out while trying to look for hidden element by %s.' % str(locator))
      raise ElementDoesNotExistAssertionError(locator)

  def _check_for_invisible_element_boolean(self, locator):
    self.set_timeout(2)
    try:
      self._wait.until(EC.invisibility_of_element_located(locator))
      return True
    except:
      return False
    finally:
      self.restore_timeout()

  def _check_for_absence_of_element(self, locator):
    self.set_timeout(1)
    try:
      return self._wait.until_not(EC.visibility_of_element_located(locator))
    except TimeoutException:
      print ('\t[WebDriver Error] Found element using %s (test was for element absence).' % str(locator))
      raise ElementExistsAssertionError(locator)
    finally:
      self.restore_timeout()

  def _gets(self, locator):
    try:
      return [x.wrapped_element for x in self._wait.until(EC.presence_of_all_elements_located(locator))]
    except TimeoutException:
      print ('\t[WebDriver Error] WebDriver timed out while trying to identify elements by %s.' % str(locator))
      raise ElementDoesNotExistAssertionError(locator)

  def _wait_for_element(self, element):
    self._wait.until(CEC.element_to_be_clickable(element))

  def _scroll_into_view(self, element):
    self._driver.execute_script("javascript:arguments[0].scrollIntoView()", element)

  def _is_link_valid(self, link):
    return self.__linkVerifier.is_link_valid(link.get_attribute('href'))

  def _is_image_valid(self, img):
    return self.__linkVerifier.is_link_valid(img.get_attribute('src'))

  def traverse_to_frame(self, frame):
    print ('\t[WebDriver] About to switch to frame "%s"...' % frame,)
    self._wait.until(EC.frame_to_be_available_and_switch_to_it(frame))
    print ('OK')

  def traverse_from_frame(self):
    print ('\t[WebDriver] About to switch to default content...',)
    self._driver.switch_to.default_content()
    print ('OK')

  def set_timeout(self, new_timeout):
    self._driver.implicitly_wait(new_timeout)
    self._wait = WebDriverWait(self._driver, new_timeout)

  def restore_timeout(self):
    self._driver.implicitly_wait(Config.wait_timeout)
    self._wait = WebDriverWait(self._driver, Config.wait_timeout)

  def get_text(self, s):
    soup = BeautifulSoup(s)
    clean_out = soup.get_text()
    print(clean_out)
    return clean_out

  def refresh(self):
    """
    refreshes the whole page
    """

    self._driver.refresh()

  def is_element_present(self, locator):
    try:
      self._driver.find_element(By.ID, locator)
      return True
    except NoSuchElementException:
      print ('\t[WebDriver] Element %s does not exist.' % str(locator))
      return False

  def is_element_present_css(self, locator):
    try:
      self._driver.find_element(By.CSS_SELECTOR, locator)
      return True
    except NoSuchElementException:
      print ('\t[WebDriver] Element %s does not exist.' % str(locator))
      return False

  def is_element_present_xpath(self, locator):
    try:
      self._driver.find_element(By.XPATH, locator)
      return True
    except NoSuchElementException:
      print ('\t[WebDriver] Element %s does not exist.' % str(locator))
      return False

  def is_element_present_class(self, locator):
    try:
      self._driver.find_element(By.CLASS_NAME, locator)
      return True
    except NoSuchElementException:
      print ('\t[WebDriver] Element %s does not exist.' % str(locator))
      return False

  def wait_for_animation(self, selector):
      while self.is_element_animated(selector):
          sleep(.5)

  def is_element_animated(self, selector):
      return self._driver.execute_script(
          'return jQuery({0}).is(":animated");'.format(json.dumps(selector)))

  def wait_until_ajax_complete(self):
    self._wait.until(lambda driver: self._driver.execute_script("return jQuery.active == 0"))

  def wait_until_image_complete(self, image):
    self._wait.until(lambda driver: self._driver.execute_script( \
        "return arguments[0].complete && typeof arguments[0].naturalWidth != \"undefined\" &&" \ 
        "arguments[0].naturalWidth > 0", image))

  def _check_element_font_weight(self, element, expected_font_weight):
    applied_font_weight = element.value_of_css_property("font-weight")
    if expected_font_weight == 'bold' or expected_font_weight == '700':
      assert applied_font_weight == 'bold' or applied_font_weight == '700', \
        'Applied font weight: %s is different from the expected: %s' % (applied_font_weight, expected_font_weight)
    elif expected_font_weight == 'normal' or expected_font_weight == '400':
      assert applied_font_weight == 'normal' or applied_font_weight == '400', \
        'Applied font weight: %s is different from the expected: %s' % (applied_font_weight, expected_font_weight)
    else:
      assert applied_font_weight == expected_font_weight, \
        'Applied font weight: %s is different from the expected: %s' % (applied_font_weight, expected_font_weight)

  def _page_ready(self, locator):
    """
    A function to validate that the dashboard page is loaded before interacting with it
    """

    self.set_timeout(5)
    try:
      self._wait_for_element(locator)
    except ElementDoesNotExistAssertionError:
      try:
        self._wait_for_element(locator)
      except ElementDoesNotExistAssertionError:
        self._wait_for_element(locator)
    self.restore_timeout()