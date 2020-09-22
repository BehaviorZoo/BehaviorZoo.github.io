# coding: utf-8
from __future__ import unicode_literals
from functools import partial

AUTHOR   = "Shuto"
SITENAME = "BehaviorZoo"
SITEURL  = "https://BehaviorZoo.github.io/"
# SITEURL = "http://127.0.0.1:8000"
SITE_LICENSE = "MIT"
# GOOGLE_ANALYTICS = "UA-XXXXXXXXX-X"
# Path to content directory to be processed by Pelican.
PATH = "."
THEME = "pelican-themes/pelican-fh5co-marble"
TIMEZONE = "Asia/Tokyo"
DEFAULT_LANG = "en"
DATE_FORMATS = {
    "en": "%a, %d %b %Y",
    "ja": "%Y-%m-%d(%a)",
}

# Specify pages
DIRECT_TEMPLATES = [
    "index", "tags", "categories", "authors", "archives", "search", 
    # "404", "top"
]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# tell pelican where your custom.css file is in your content folder
STATIC_PATHS = ["static"]
# tell pelican where it should copy that file to in your output folder
EXTRA_PATH_METADATA = {
    "static/custom.css": {"path": "theme/css/custom.css"}
}
# tell the pelican-bootstrap-3 theme where to find the custom.css file in your output folder
CUSTOM_CSS = "theme/css/custom.css"

# PLUGINS
PLUGIN_PATHS = ["./pelican-plugins"]
PLUGINS = ["i18n_subsites", "render_math", "tipue_search", "encrypt_content", "neighbors"] # "cover-image"]
# jupyter notebook
MARKUP = ("md", "ipynb")
IGNORE_FILES = [".ipynb_checkpoints", ".DS_Store"]
IPYNB_SKIP_CSS = True   # Do not use Ipython CSS.
IPYNB_IGNORE_CSS = True # Suppress the inclusion of CSS entirely
# i18n_subsites
JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.i18n"],
}

# Encrypt Pelican Content
ENCRYPT_CONTENT = {
    "title_prefix": '<i class="fas fa-lock"></i>',
    "summary": "This content is encrypted."
}

# COVER_IMAGE
# COVER_IMAGES_PATH = "theme/cover_images"
# DEFAULT_COVER_IMAGE = "default_image.png"

# Blogroll
# LINKS = (("Home",       "https://iwasakishuto.github.io"),
#          ("Blog",       "https://iwasakishuto.github.io/blog/articles/index.html"),
#          ("University", "https://iwasakishuto.github.io/University/index.html"),
#          ("Kerasy",     "https://iwasakishuto.github.io/Kerasy/doc/index.html"),
#          ("Front-End",  "https://iwasakishuto.github.io/Front-End/index.html"))
# Social widget
SOCIAL = (("twitter",  "https://twitter.com/cabernet_rock"),
          ("github",   "https://github.com/iwasakishuto"),
          ("facebook", "https://www.facebook.com/iwasakishuto"))

DEFAULT_PAGINATION = 10
TWITTER_USERNAME = "cabernet_rock"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

JINJA_FILTERS = {
    "sort_by_article_count": partial(sorted,
        key = lambda tags: -len(tags[1])) # tags = (tag, articles)
}
