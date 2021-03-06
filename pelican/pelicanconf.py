# coding: utf-8
from __future__ import unicode_literals
from functools import partial
from urllib.parse import urljoin

AUTHOR   = "Shuto"
SITENAME = "BehaviorZoo"
SITEURL  = "https://BehaviorZoo.github.io"
SITE_LICENSE = "MIT"
GOOGLE_TRACKING_ID = "UA-180584889-1"
THEME = "pelican-fh5co-marble-modified"
TIMEZONE = "Asia/Tokyo"
DEFAULT_LANG = "en"
DATE_FORMATS = {
    "en": "%a, %d %b %Y",
    "ja": "%Y-%m-%d(%a)",
}
ABOUT = {
  "mail"    : "cabernet.rock@gmail.com",
  "image"   : "https://pbs.twimg.com/profile_images/1254020323428544513/_azsW438_400x400.jpg",
  "address" : "The University of Tokyo, 7-chōme-3-1 Hongō, Bunkyo City, Tokyo 113-8654, Japan",
  "phone"   : "090-XXXX-XXXX",
}
PATH = "."
STATIC_PATHS = ["theme", "thumbnails"]
EXTRA_PATH_METADATA = {
    "theme/css"    : {"path": "theme/css"},
    "theme/js"     : {"path": "theme/js"},
    "theme/images" : {"path": "theme/images"},
}
LOGO             = urljoin(base=SITEURL, url="theme/images/logo-round.png")
APPLE_TOUCH_ICON = urljoin(base=SITEURL, url="theme/images/apple-touch-icon.png")
IMAGE_NOT_FOUND  = urljoin(base=SITEURL, url="theme/images/image-not-found.png")
USE_FOLDER_AS_CATEGORY = True
# Specify pages
DIRECT_TEMPLATES = [
    "index", "tags", "categories", "archives", "search", "404", "contact",
]
DEFAULT_PAGINATION = 100
DISQUS_ON_PAGES = False
# Feed generation
FEED_DOMAIN        = SITEURL
FEED_ALL_ATOM      = "feeds/all.atom.xml"
TAG_FEED_ATOM      = "feeds/{slug}.tag.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
# Markdown extension
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
            'linenums': False,
            'use_pygments': False,
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.tables': {},
        'markdown.extensions.fenced_code': {},
        'markdown.extensions.admonition': {},
    },
    'output_format': 'html5',
}
# Plugins
from pelican_jupyter import markup as nb_markup
PLUGIN_PATHS = ["./pelican-plugins-modified"]
PLUGINS = ["i18n_subsites", nb_markup, "render_math", "tipue_search", "neighbors", "pelican-datatable"]
# i18n_subsites
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
# I18N_SUBSITES = {
#     'de': {
#         'SITENAME': 'Testseite',
#         'AUTHOR': 'Der Tester',
#         'LOCALE': 'de_DE.UTF-8',
#     },
#     'fr': {}
# }

# jupyter notebook
MARKUP = ("md", "ipynb")
IGNORE_FILES = [".ipynb_checkpoints", ".DS_Store"]
IPYNB_SKIP_CSS = True   # Do not use Ipython CSS.
IPYNB_IGNORE_CSS = True # Suppress the inclusion of CSS entirely
# Social Widget
SOCIAL = (
    ("twitter",  "https://twitter.com/cabernet_rock"),
    ("github",   "https://github.com/BehaviorZoo")
)
TWITTER_USERNAME = "cabernet_rock"
# Sort tags by the number of atricles. (Descending Order)
JINJA_FILTERS = {
    "sort_by_article_count": partial(sorted, key=lambda tags: -len(tags[1])) # tags = (tag, articles)
}
