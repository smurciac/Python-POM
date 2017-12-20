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
from .WombatPage import WombatPage

class HomePage(WombatPage):
  """
  Model an abstract base Journal page.
  """

  def __init__(self, driver, url_suffix=''):
    super(HomePage, self).__init__(driver, url_suffix)

    # Locators - Instance members
    self._locator_by_id = (By.ID, "hero")
    self._locator_by_css = (By.CSS_SELECTOR, "#article-list h3")
    self._locator_by_xpath = (By.XPATH, '//div[@id=\'article-list\']/section/ul/li')

  # POM Actions
  def validate_locator_by_id(self):
    self._get(self._locator_by_id)
    #Here we can put some interactions like .click()
    return self

  def validate_tier1(self):
    self._get(self._locator_by_css)
    # Here we can put some interactions like .click()
    return self

  def validate_tier2(self):
    self._get(self._locator_by_xpath)
    # Here we can put some interactions like .click()
    return self