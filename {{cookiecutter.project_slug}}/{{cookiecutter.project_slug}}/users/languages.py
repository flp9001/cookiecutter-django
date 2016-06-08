# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# List of language code and languages local names.
#
# This list is output of code:
# [
#     (code, get_language_info(code).get("name_local"))
#     for code, lang in settings.LANGUAGES
# ]
#
# List is stored here instead of getting it on runtime because
# there was changes in that list between Django version 1.7 and 1.8.
# This in turn causes Django 1.7 to think that there is unmigrated changes

LANGUAGES = [
    ("en", "English"),
    ("es", "Español"),
    ("pt-br", "Português Brasileiro"),
]
