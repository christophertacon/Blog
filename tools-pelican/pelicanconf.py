#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'NGCM CDT'  #Denis Kramer, Ian Hawke, Peter Horak, Hans Fangohr'
SITENAME = u'Computational Modelling Tools Workshops'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
           ('NGCM Blog', 'http://www.ngcm.soton.ac.uk/blog/'),
           ('CMG', 'http://cmg.soton.ac.uk/'),
           ('Uni Southampton', 'http://www.southampton.ac.uk')
        )

# Social widget
SOCIAL = (('NGCM Twitter', 'https://twitter.com/NGCM_Soton'),
          )

DEFAULT_PAGINATION = False

DEFAULT_CATEGORY = 'Tools'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME="themes/notmyidea"

MENUITEMS = [('About', 'about.html'),
            ('Archive', 'archives.html'),
             ('Tags', 'tags.html')
             ]

STATIC_PATHS = ['.', 'images', 'notebooks', 'content']

# use paths in main directory to avoid subdirectory confusion
CATEGORY_URL = 'category-{slug}.html'
CATEGORY_SAVE_AS = 'category-{slug}.html'

TAG_URL = 'tag-{slug}.html'
TAG_SAVE_AS = 'tag-{slug}.html'

AUTHOR_URL = 'author-{slug}.html'
AUTHOR_SAVE_AS = 'author-{slug}.html'

LOAD_CONTENT_CACHE = False

DISPLAY_CATEGORIES_ON_MENU = False

# --------------- PLUGINS ---------------
# Define a path to the plugins directory:
PLUGIN_PATHS = ["plugins"]

# List the plugins you want to use:
PLUGINS = [	'keyboard.kb',
			'html_rst_directive']