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

import logging
from os import getenv

from selenium.webdriver import DesiredCapabilities

# === Logging Level ===
logging.basicConfig(level=logging.INFO)

# === WebDriver specific section ===

# WebDriver's implicit timeout (in seconds)
wait_timeout = 60

# WebDriver's Page Load timeout (in seconds)
page_load_timeout = 60

# Framework's link verification timeout (in seconds)
verify_link_timeout = 5

# Framework's link verification retries
verify_link_retries = 5

# Framework's link verification wait time between retries (in seconds)
wait_between_retries = 3

"""
Set **WEBDRIVER_ENVIRONMENT** env variable/default value to one of these:

1. **prod** will run tests against **PRODUCTION** site (each POM should know it prod site)
2. **dev** will run tests against the site defined by `base_url` variable.

When **WEBDRIVER_ENVIRONMENT** is set to "prod" then **WEBDRIVER_TARGET_URL** is ignored

Set **WEBDRIVER_TARGET_URL** env variable/default value to desired URL to run suite against it
when **WEBDRIVER_ENVIRONMENT** is `dev`
"""

#Environment variables
environment = getenv('WEBDRIVER_ENVIRONMENT', 'prod')
base_url = getenv('WEBDRIVER_TARGET_URL', 'http://somethinghere.com')
rhino_url = getenv('RHINO_URL', 'http://somethinghere.com')
collections_url = getenv('WEBDRIVER_COLLECTIONS_URL', 'http://somethinghere.com')
base_url_mobile = getenv('WEBDRIVER_MOBILE_TARGET_URL', 'http://somethinghere.com')
existing_user_email = getenv('WEBDRIVER_USER_EMAIL', 'user@testmail.com')
existing_user_pw = getenv('WEBDRIVER_USER_PASSWORD', 'password')
device_type = getenv('WEBDRIVER_DEVICE_TYPE', 'desktop')

"""
Create a DB Configuration for use my MySQL.py
"""

dbconfig = {'user': mysql_user,
            'password': mysql_password,
            'host': mysql_host,
            'port': 3306,
            'database': 'DBNAME',
            'connection_timeout': 10
            }

repo_config = {'transport': 'http',
               'host': crepo_host,
               'port': crepo_port,
               'path': '/v1',
               }

# === Appium (stand-alone) module configuration section ===

"""
Since a Macintosh box can run both Android SDK & VMs *and* IOS Simulator it would be wise to
have Appium deployed on Macintosh hardware.

But in case it is not possible, you can still point to an Appium node for Android and a different
one for IOS, separately.
"""

run_against_appium = getenv('USE_APPIUM_SERVER', False)
appium_android_node_url = getenv('APPIUM_NODE_URL', 'androidnode/wd/hub')
appium_ios_node_url = getenv('APPIUM_NODE_URL', 'http://iosnode/wd/hub')

# **Android** capabilities definition
ANDROID = {
  'browserName': 'Browser',
  'platformName': 'Android',
  'platformVersion': '4.4',
  'deviceName': 'Android Emulator'
}

# **iOS** capabilities definition
IOS = {
  'browserName': 'Safari',
  'platformName': 'iOS',
  'platformVersion': '7.1',
  'deviceName': 'iPhone Simulator'
}

# List of Appium (stand-alone mode) enabled browsers
appium_enabled_browsers = [
  ANDROID,
  IOS
]

# === Selenium Grid configuration section ===

"""
Set **USE_SELENIUM_GRID** env variable/default value to desired one of these:

1. **True** will run tests against ALL browsers in Selenium Grid
2. **False** will run tests against your local **Firefox** browser

Set **SELENIUM_GRID_URL** env variable/default value to point to Grid hub node.

Running through Grid **takes precedence** among all other configurations.

Ex: If you have both `USE_APPIUM_SERVER` **AND** `USE_SELENIUM_GRID` options set to **True**,
then tests will be run against the **Grid**.

You can *still* include IOS and ANDROID capabilities as *enabled browsers* in the Grid and will be run against Appium.

"""

run_against_grid = getenv('USE_SELENIUM_GRID', False)
selenium_grid_url = getenv('SELENIUM_GRID_URL', 'http://seleniumgridurl/wd/hub')

"""

List of all browsers enabled in the **Selenium Grid**.
Ignored when **run_against_grid** is set to **False**.

"""

grid_enabled_browsers = [
  DesiredCapabilities.FIREFOX,
  DesiredCapabilities.INTERNETEXPLORER,
  DesiredCapabilities.CHROME,
  DesiredCapabilities.SAFARI,
  IOS,
  ANDROID
]

"""
Defines the single browser with which we would like to run the test suite.
If no environment variable is defined, default to FIREFOX.
"""

browser = getenv('SELENIUM_BROWSER_TO_USE', 'FIREFOX')

# === Performance metric gathering configuration section ===

"""

Set **browsermob_proxy_enabled** to either *True* or *False* to enable or disable the use of
**BrowserMob Proxy** to gather performance metrics while the tests navigate the web sites.

Set **browsermob_proxy_path** variable to the path of the **BrowserMob Proxy** *binary* in your
machine.

"""
browsermob_proxy_enabled = getenv('USE_BROWSERMOB_PROXY', False)
browsermob_proxy_path = '/opt/browsermob/bin/browsermob-proxy'