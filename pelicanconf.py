#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Alex Gose'
SITENAME = 'Alex Gose'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://linkedin.com/in/alexgose'),
        ('github', 'https://github.com/alexgose'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = 'themes/pelican-bootstrap3'
PLUGIN_PATHS = ['plugins/', ]
PLUGINS = ['i18n_subsites', 'render_math', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

USE_FOLDER_AS_CATEGORY = True

CC_LICENSE = "CC-BY-SA"
GITHUB_USER = "AlexGose"
DISPLAY_ARTICLE_INFO_ON_INDEX = True
