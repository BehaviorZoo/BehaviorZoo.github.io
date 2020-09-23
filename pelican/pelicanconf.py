# coding: utf-8
from __future__ import unicode_literals
from functools import partial


# ===================== #
# ENVIRONMENT VARIABLES #
# ===================== #
AUTHOR   = "Shuto"
SITENAME = "BehaviorZoo"
SITEURL  = "https://BehaviorZoo.github.io"
SITE_LICENSE = "MIT"
TIMEZONE = "Asia/Tokyo"
DEFAULT_LANG = "en"
DATE_FORMATS = {
    "en": "%a, %d %b %Y",
    "ja": "%Y-%m-%d(%a)",
}
THEME = "pelican-themes/pelican-fh5co-marble"
# GOOGLE_ANALYTICS = "UA-XXXXXXXXX-X"
DEFAULT_PAGINATION = 10
# Specify pages
DIRECT_TEMPLATES = [
    "index", "tags", "categories", "authors", "archives", "search", 
    # "404", "top"
]
# Sort tags by the number of atricles. (Descending Order)
JINJA_FILTERS = {
    "sort_by_article_count": partial(sorted,
        key = lambda tags: -len(tags[1])) # tags = (tag, articles)
}


# ======== #
#   PATH   #
# ======== #
# Path to content directory to be processed by Pelican.
PATH = "." 
# A list of directories (relative to PATH) in which to look for static files. 
# Such files will be copied to the output directory without modification.
STATIC_PATHS = ["_static"]
EXTRA_PATH_METADATA = {
    "_static/behaviorzoo.css": {"path": "theme/css/behaviorzoo.css"}
}

# =============== #
# FEED GENERATION #
# =============== #
FEED_ALL_ATOM         = None
CATEGORY_FEED_ATOM    = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM      = None
AUTHOR_FEED_RSS       = None


# =========== #
#   PLUGINS   #
# =========== #
PLUGIN_PATHS = ["./pelican-plugins"]
PLUGINS = [
    "i18n_subsites", "render_math", "tipue_search", "neighbors"
]
# jupyter notebook
MARKUP = ("md", "ipynb")
IGNORE_FILES = [".ipynb_checkpoints", ".DS_Store"]
IPYNB_SKIP_CSS = True   # Do not use Ipython CSS.
IPYNB_IGNORE_CSS = True # Suppress the inclusion of CSS entirely
# i18n_subsites
JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.i18n"],
}


# ================= #
#   Social Widget   #
# ================= #
TWITTER_USERNAME = "cabernet_rock"
SOCIAL = (
    ("twitter",  "https://twitter.com/cabernet_rock"),
    ("github",   "https://github.com/BehaviorZoo")
)