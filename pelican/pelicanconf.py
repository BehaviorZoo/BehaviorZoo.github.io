# coding: utf-8
from __future__ import unicode_literals
from functools import partial
from urllib.parse import urljoin

AUTHOR   = "Shuto"
SITENAME = "BehaviorZoo"
SITEURL  = "https://BehaviorZoo.github.io"
SITE_LICENSE = "MIT"
# GOOGLE_ANALYTICS = "UA-XXXXXXXXX-X"
THEME = "pelican-fh5co-marble-modified"
TIMEZONE = "Asia/Tokyo"
DEFAULT_LANG = "en"
DATE_FORMATS = {
    "en": "%a, %d %b %Y",
    "ja": "%Y-%m-%d(%a)",
}
PATH = "."
STATIC_PATHS = ["static"]
THUMBNAILS_DIR = "theme/thumbnails"
EXTRA_PATH_METADATA = {
    "static/behaviorzoo.css" : {"path": "theme/css/behaviorzoo.css"},
    "static/images"          : {"path": "theme/images"},
    "static/thumbnails"      : {"path": THUMBNAILS_DIR},
}
LOGO             = urljoin(base=SITEURL, url="theme/images/logo-round.png")
APPLE_TOUCH_ICON = urljoin(base=SITEURL, url="theme/images/apple-touch-icon.png")
THUMBNAILS_URL   = urljoin(base=SITEURL, url=THUMBNAILS_DIR)
USE_FOLDER_AS_CATEGORY = True
# Specify pages
DIRECT_TEMPLATES = [
    "index", "tags", "categories", "archives", "search", "404", 
]
DEFAULT_PAGINATION = 10
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
PLUGINS = ["i18n_subsites", nb_markup, "render_math", "tipue_search", "neighbors"]
# jupyter notebook
MARKUP = ("md", "ipynb")
IGNORE_FILES = [".ipynb_checkpoints", ".DS_Store"]
IPYNB_SKIP_CSS = True   # Do not use Ipython CSS.
IPYNB_IGNORE_CSS = True # Suppress the inclusion of CSS entirely
# i18n_subsites
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
# Social Widget
SOCIAL = (
    ("twitter",  "https://twitter.com/cabernet_rock"),
    ("github",   "https://github.com/BehaviorZoo")
)
TWITTER_USERNAME = "cabernet_rock"
# Sort tags by the number of atricles. (Descending Order)
JINJA_FILTERS = {
    "sort_by_article_count": partial(sorted,
        key = lambda tags: -len(tags[1])) # tags = (tag, articles)
}
