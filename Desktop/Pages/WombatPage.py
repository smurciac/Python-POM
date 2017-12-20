#!/usr/bin/env python2
# -*- coding: utf-8 -*-

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

from selenium.webdriver.common.by import By
from ...Base.PomPage import PomPage

# Variable definitions

class WombatPage(PomPage):
  """
  Model an abstract base Wombat page for desktop
  """

  expected_isc_link = 'http://www.isc.org/'

  expected_privacy_link = 'https://www.plos.org/privacy-policy'

  expected_terms_link = 'https://www.plos.org/terms-of-use'

  expected_copyright_link = 'https://www.plos.org/copyright'

  expected_ads_link = 'https://www.plos.org/advertise/'

  expected_media_link = 'https://www.plos.org/media-inquiries'

  expected_pubs_link = 'https://www.plos.org/publications/journals/'

  expected_pbio_link = 'http://journals.plos.org/plosbiology/'

  expected_pmed_link = 'http://journals.plos.org/plosmedicine/'

  expected_pcbi_link = 'http://journals.plos.org/ploscompbiol/'

  expected_pcur_link = 'http://currents.plos.org/'

  expected_pgen_link = 'http://journals.plos.org/plosgenetics/'

  expected_ppat_link = 'http://journals.plos.org/plospathogens/'

  expected_pone_link = 'http://journals.plos.org/plosone/'

  expected_pntd_link = 'http://journals.plos.org/plosntds/'

  expected_porg_link = 'https://www.plos.org/'

  expected_blog_link = 'http://blogs.plos.org/'

  expected_coll_link = 'http://collections.plos.org/'

  expected_feedback_link = '/feedback/new'

  expected_help_link = '/s/help-using-this-site'

  expected_lockss_link = '/lockss-manifest'

  expected_ca_corp_stmt = 'PLOS is a nonprofit 501(c)(3) corporation, #C2354500, and is based in San Francisco, California, US'

  def __init__(self, driver, url_suffix=''):
    super(WombatPage, self).__init__(driver, url_suffix)

    # Locators - Instance members
    self._nav_user = (By.ID, 'user')
    self._sign_in_link = (By.XPATH, '//li[@class="highlighted"]/a')
    self._nav_main = (By.ID, 'pagehdr')
    self._logo = (By.XPATH, "//li[@class='home-link']")
    self._search_widget = (By.XPATH, "//button[@type='submit']")

    self._publish_menu_ambra = (By.ID, "mn-02")
    self._publish_menu = (By.ID, 'publish')

    self._about_menu_ambra = (By.ID, "mn-03")
    self._about_menu = (By.ID, 'about')

    self._browse_menu = (By.ID, "browse")
    self._browse_menu_ambra = (By.ID, "browse")

    self._for_authors_menu = (By.ID, "for-authors")

    self._page_footer = (By.CSS_SELECTOR, '#pageftr > .row')

    self._footer_logo = (By.CLASS_NAME, 'logo-footer')
    self._footer_logo_ambra = (By.CLASS_NAME, 'logo')

    self._footer_version = (By.CSS_SELECTOR, 'p[class="nav-special"] > a')
    self._footer_version_ambra = (By.CSS_SELECTOR, 'div[class="col col-1"] > p > a')

    self._footer_isc_link = (By.XPATH, '//p[@class="nav-special"]/a[2]')
    self._footer_isc_link_ambra = (By.XPATH, '//div[@class="col col-1"]/p/a[2]')

    self._footer_privacy_policy_link = (By.CSS_SELECTOR, '#ftr-privacy')
    self._footer_privacy_policy_link_ambra = (By.CSS_SELECTOR, 'div[class="nav nav-aux"] > a')

    self._footer_terms_of_use_link = (By.CSS_SELECTOR, '#ftr-terms')
    self._footer_terms_of_use_link_ambra = (By.XPATH, '//div[@class="nav nav-aux"]/a[2]')

    self._footer_copyright_link = (By.CSS_SELECTOR, '#ftr-copyright')

    self._footer_advertise_link = (By.CSS_SELECTOR, '#ftr-advertise')
    self._footer_advertise_link_ambra = (By.XPATH, '//div[@class="nav nav-aux"]/a[3]')

    self._footer_media_inquiries_link = (By.CSS_SELECTOR, '#ftr-media')
    self._footer_media_inquiries_link_ambra = (By.XPATH, '//div[@class="nav nav-aux"]/a[4]')

    self._footer_publications_link = (By.CSS_SELECTOR, 'div[class="link-column"] > p[class="nav-special"] > a')
    self._footer_publications_link_ambra = (By.CSS_SELECTOR, 'div[class="col col-2"] > p > a')

    self._footer_pbio_link = (By.CSS_SELECTOR, 'div[class="link-column"] > div[class="nav"] > ul > li > a')
    self._footer_pbio_link_ambra = (By.CSS_SELECTOR, 'div[class="col col-2"] > div[class="nav"] > ul > li > a')

    self._footer_pmed_link = (By.XPATH, '//div[@class="link-column"]/div[@class="nav"]/ul/li[2]/a')
    self._footer_pmed_link_ambra = (By.XPATH, '//div[@class="col col-2"]/div[@class="nav"]/ul/li[2]/a')

    self._footer_pcbi_link = (By.XPATH, '//div[@class="link-column"]/div[@class="nav"]/ul/li[3]/a')
    self._footer_pcbi_link_ambra = (By.XPATH, '//div[@class="col col-2"]/div[@class="nav"]/ul/li[3]/a')

    self._footer_pcur_link = (By.XPATH, '//div[@class="link-column"]/div[@class="nav"]/ul/li[4]/a')
    self._footer_pcur_link_ambra = (By.XPATH, '//div[@class="col col-2"]/div[@class="nav"]/ul/li[4]/a')

    self._footer_pgen_link = (By.XPATH, '//div[@class="link-column"]/div[@class="nav"]/ul/li[5]/a')
    self._footer_pgen_link_ambra = (By.XPATH, '//div[@class="col col-2"]/div[@class="nav"]/ul/li[5]/a')

    self._footer_ppat_link = (By.XPATH, '//div[@class="link-column"]/div[@class="nav"]/ul/li[6]/a')
    self._footer_ppat_link_ambra = (By.XPATH, '//div[@class="col col-2"]/div[@class="nav"]/ul/li[6]/a')

    self._footer_pone_link = (By.XPATH, '//div[@class="link-column"]/div[@class="nav"]/ul/li[7]/a')
    self._footer_pone_link_ambra = (By.XPATH, '//div[@class="col col-2"]/div[@class="nav"]/ul/li[7]/a')

    self._footer_pntd_link = (By.XPATH, '//div[@class="link-column"]/div[@class="nav"]/ul/li[8]/a')
    self._footer_pntd_link_ambra = (By.XPATH, '//div[@class="col col-2"]/div[@class="nav"]/ul/li[8]/a')

    self._footer_porg_link = (By.XPATH, '//footer/div/div[3]/div/p/a')
    self._footer_porg_link_ambra = (By.XPATH, '//div[@class="col col-3"]/div[@class="nav"]/p/a')

    self._footer_blog_link = (By.XPATH, '//footer/div/div[3]/div/p[2]/a')
    self._footer_blog_link_ambra = (By.XPATH, '//div[@class="col col-3"]/div[@class="nav"]/p[2]/a')

    self._footer_coll_link = (By.XPATH, '//footer/div/div[3]/div/p[3]/a')
    self._footer_coll_link_ambra = (By.XPATH, '//div[@class="col col-3"]/div[@class="nav"]/p[3]/a')

    self._footer_feedback_link = (By.XPATH, '//footer/div/div[3]/div/p[4]/a')
    self._footer_feedback_link_ambra = (By.XPATH, '//div[@class="col col-3"]/div[@class="nav"]/p[4]/a')

    self._footer_help_link = (By.XPATH, '//footer/div/div[3]/div/p[5]/a')
    self._footer_help_link_ambra = (By.XPATH, '//div[@class="col col-3"]/div[@class="nav"]/p[5]/a')

    self._footer_lockss_link = (By.ID, 'ftr-lockss')

    self._footer_ca_corp_stmt = (By.XPATH, '//footer/div/div[3]/div/p[7]')
    self._footer_ca_corp_stmt_ambra = (By.XPATH, '//div[@class="col col-3"]/div[@class="nav"]/p[6]/a')

  # POM Actions

  def validate_sign_in_button(self):
    self._get(self._nav_user).find_element_by_partial_link_text('sign in')
    return self

  def is_user_logged(self):
    btn = self._get(self._nav_user).find_element_by_css_selector('.highlighted a')
    return btn.text == 'sign out'

  def click_sign_in(self):
    sign_in_link = self._get(self._nav_user).find_element(*self._sign_in_link)
    sign_in_link.click()
    return self

  def validate_sign_out_button(self):
    self._get(self._nav_user).find_element_by_partial_link_text('sign out')
    return self

  def click_sign_out(self):
    sign_out_link = self._get(self._nav_user).find_element_by_partial_link_text('sign out')
    sign_out_link.click()
    return self

  def click_logo(self):
    logo_link = self._get(self._nav_main).find_element(*self._logo)
    logo_link.click()
    return self

  def click_search_widget(self):
    swidget_link = self._get(self._nav_main).find_element(*self._search_widget)
    swidget_link.click()
    return self

  def hover_browse(self):
    browse = self._get(self._browse_menu)
    self._actions.move_to_element(browse).perform()
    return self

  def hover_browse_ambra(self):
    browse = self._get(self._browse_menu_ambra)
    self._actions.move_to_element(browse).perform()
    return self

  def hover_publish(self):
    publish = self._get(self._publish_menu)
    self._actions.move_to_element(publish).perform()
    return self

  def hover_publish_ambra(self):
    publish = self._get(self._publish_menu_ambra)
    self._actions.move_to_element(publish).perform()
    return self

  def hover_about(self):
    about = self._get(self._about_menu)
    self._actions.move_to_element(about).perform()
    return self

  def hover_about_ambra(self):
    about = self._get(self._about_menu_ambra)
    self._actions.move_to_element(about).perform()
    return self

  def moveto_footer(self):
    footer = self._get(self._page_footer)
    self._scroll_into_view(footer)
    return self

  def validate_footer_logo(self):
    self._get(self._footer_logo)
    return self

  def validate_footer_nav_aux(self):
    """
    The footer implementation is split into four different sections. nav_aux contains the horizontal links
    along the left bottom of the footer.
    Validate the links point to the right place.
    :return: success/assertion exception
    """

    privacy_link = self._get(self._footer_privacy_policy_link).get_attribute('href')
    assert privacy_link == self.expected_privacy_link, '%s not equal to expected %s' % (privacy_link,
                                                                                        self.expected_privacy_link)
    terms_link = self._get(self._footer_terms_of_use_link).get_attribute('href')
    assert terms_link == self.expected_terms_link, '%s not equal to expected %s' % (terms_link,
                                                                                    self.expected_terms_link)
    copyright_link = self._get(self._footer_copyright_link).get_attribute('href')
    assert copyright_link == self.expected_copyright_link, '%s not equal to expected %s' % (copyright_link,
                                                                                            self.expected_copyright_link)
    ads_link = self._get(self._footer_advertise_link).get_attribute('href')
    assert ads_link == self.expected_ads_link, '%s not equal to expected %s' % (ads_link, self.expected_ads_link)
    media_link = self._get(self._footer_media_inquiries_link).get_attribute('href')
    assert media_link == self.expected_media_link, '%s not equal to expected %s' % (media_link,
                                                                                    self.expected_media_link)
    return self

  def validate_footer_link_column_one(self):
    """
    The footer implementation is split into four different sections. footer link column one contains the first set of
    vertical links pointing at the various PLOS publications.
    Validate the links point to the correct place.
    :return: success/assertion exception
    """

    pubs_link = self._get(self._footer_publications_link).get_attribute('href')
    assert pubs_link == self.expected_pubs_link, '%s not equal to expected %s' % (pubs_link, self.expected_pubs_link)
    pbio_link = self._get(self._footer_pbio_link).get_attribute('href')
    assert pbio_link == self.expected_pbio_link, '%s not equal to expected %s' % (pbio_link, self.expected_pbio_link)
    pmed_link = self._get(self._footer_pmed_link).get_attribute('href')
    assert pmed_link == self.expected_pmed_link, '%s not equal to expected %s' % (pmed_link, self.expected_pmed_link)
    pcbi_link = self._get(self._footer_pcbi_link).get_attribute('href')
    assert pcbi_link == self.expected_pcbi_link, '%s not equal to expected %s' % (pcbi_link, self.expected_pcbi_link)
    pcur_link = self._get(self._footer_pcur_link).get_attribute('href')
    assert pcur_link == self.expected_pcur_link, '%s not equal to expected %s' % (pcur_link, self.expected_pcur_link)
    pgen_link = self._get(self._footer_pgen_link).get_attribute('href')
    assert pgen_link == self.expected_pgen_link, '%s not equal to expected %s' % (pgen_link, self.expected_pgen_link)
    ppat_link = self._get(self._footer_ppat_link).get_attribute('href')
    assert ppat_link == self.expected_ppat_link, '%s not equal to expected %s' % (ppat_link, self.expected_ppat_link)
    pone_link = self._get(self._footer_pone_link).get_attribute('href')
    assert pone_link == self.expected_pone_link, '%s not equal to expected %s' % (pone_link, self.expected_pone_link)
    pntd_link = self._get(self._footer_pntd_link).get_attribute('href')
    assert pntd_link == self.expected_pntd_link, '%s not equal to expected %s' % (pntd_link, self.expected_pntd_link)
    return self

  def validate_footer_link_column_two(self):
    """
    The footer implementation is split into four different sections. footer link column two contains the rightmost set
    of vertical links pointing at the various PLOS apocryphal sites.
    Validate the links point to the correct place.
    :return: success/assertion exception
    """

    porg_link = self._get(self._footer_porg_link).get_attribute('href')
    assert porg_link == self.expected_porg_link, '%s not equal to expected %s' % (porg_link, self.expected_porg_link)
    blog_link = self._get(self._footer_blog_link).get_attribute('href')
    assert blog_link == self.expected_blog_link, '%s not equal to expected %s' % (blog_link, self.expected_blog_link)
    coll_link = self._get(self._footer_coll_link).get_attribute('href')
    assert coll_link == self.expected_coll_link, '%s not equal to expected %s' % (coll_link, self.expected_coll_link)
    help_link = self._get(self._footer_help_link).get_attribute('href')
    local_help_link = '/' + '/'.join(help_link.rsplit('/')[-2:])
    assert local_help_link == self.expected_help_link, '%s not equal to expected %s' % (local_help_link,
                                                                                        self.expected_help_link)

    lockss_link = self._get(self._footer_lockss_link).get_attribute('href')
    relative_locks_href = '/' + lockss_link.rsplit('/')[-1]
    assert relative_locks_href == self.expected_lockss_link, '%s not equal to exepcted %s' % (relative_locks_href,
                                                                                              self.expected_lockss_link)

    ca_corp_stmt = self._get(self._footer_ca_corp_stmt).text
    assert ca_corp_stmt == self.expected_ca_corp_stmt, '%s not equal to expected %s' % (ca_corp_stmt,
                                                                                        self.expected_ca_corp_stmt)
    return self