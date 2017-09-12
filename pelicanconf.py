#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys
sys.path.append('../pelican-plugins/')

from embedly_cards import EmbedlyCardExtension
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
    'extensions': [EmbedlyCardExtension()],
}

AUTHOR = u'x100krocia'
SITENAME = u'Jadę Sama'
SITEURL = ''
OUTPUT_PATH='output'

PATH = 'content'
STATIC_PATHS = ['images', 'maps']
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']
DEFAULT_CATEGORY = 'O mnie'

SLUGIFY_SOURCE = 'basename'

ARTICLE_URL = 'wyprawy/{suburl}/{slug}.html'
ARTICLE_SAVE_AS = 'wyprawy/{suburl}/{slug}.html'

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

AUTHOR_URL=''
AUTHOR_SAVE_AS=''
AUTHORS_SAVE_AS = ''

TAG_URL='tag/{slug}.html'
TAG_SAVE_AS='tag/{slug}.html'
TAGS_SAVE_AS='tagi.html'

CATEGORY_URL = 'wyprawy/{slug}.html'
CATEGORY_SAVE_AS = 'wyprawy/{slug}.html'
CATEGORIES_SAVE_AS = 'wyprawy.html'

SUBCATEGORY_URL = 'wyprawy/{fullurl}.html'
SUBCATEGORY_SAVE_AS = 'wyprawy/{fullurl}.html'
# SUBCATEGORIES_SAVE_AS = 'miejsca.html'

TIMEZONE = 'Asia/Singapore'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_LANG = u'pl'
LOCALE=['plk_pol','pl_PL']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_HOME = False

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('github', 'http://github.com/jade-sama'),)

DEFAULT_PAGINATION = 100

THEME = "../my-pelican-themes/blue-penguin-modified"
DIRECT_TEMPLATES = ['index', 'categories', 'subcategories','tags']

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['subcategory',
           'photos',
           'embedly_cards']

PHOTO_LIBRARY = "~/Pictures/blogs"
PHOTO_GALLERY = (1024, 768, 80)
PHOTO_ARTICLE = (760, 506, 80)
PHOTO_THUMB = (192, 144, 60)
PHOTO_WATERMARK = False
PHOTO_EXIF_REMOVE_GPS = True
PHOTO_EXIF_COPYRIGHT = 'CC-BY-NC'
PHOTO_EXIF_COPYRIGHT_AUTHOR = 'x100krocia'
RESPONSIVE_IMAGES = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
