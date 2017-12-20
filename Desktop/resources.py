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

from Base.Config import environment
from Base.Config import rhino_url


friendly_test_hostname = environment
if friendly_test_hostname == 'prod':
  base_url = ''
  rhino_url = rhino_url
elif friendly_test_hostname == 'localhost':
  base_url = 'http://lsomethinghere.com'
  rhino_url = 'http://something-' + friendly_test_hostname + '.here.com'

journals = [
    {'journalKey': 'One', 'journalTitle': 'One'},
    {'journalKey': 'Two', 'journalTitle': 'Two'},
    {'journalKey': 'Three', 'journalTitle': 'Three'},
]

sevenjournals = [
    { 'journalKey': 'One',
      'rhinoJournalKey': 'One',
      'journalTitle': 'One',
    },
    { 'journalKey': 'Two',
      'rhinoJournalKey': 'Two',
      'journalTitle': 'Two',
    },
    { 'journalKey': 'Three',
      'rhinoJournalKey': 'Three',
      'journalTitle': 'Three',
    }
]

# Header resources
search_term = 'Something'
search_term_root = 'Something'
searchterms = [ 'One Thing', 'Two Things', 'Three Things']

# registration resources
non_existing_user_email = 'test@email.com'
existing_user_email = 'test@email.com'
existing_user_pw = 'password'
new_user_id_local_base = 'test_user'
new_user_id_domain = '@email.com'
new_user_id_index = 250

#doi.org text url
dx_doi_url = 'https://doi.org/'