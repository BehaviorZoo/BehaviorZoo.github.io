#### Required metadata

Articles (`.md`) in `content` directory are required to have the following metadata.

```md
Title: My super title
Slug: my-super-post
Date: When the datasets were released.
Tags: tag1, tag2
Authors: Authors of the datasets.
animal: animal1, animal2
species: species1, species2
thumbnails: path2img1, path2img2
dataset_type: body_shape
```

#### Directory structure

list contents of this directories in a tree-like format.

```sh
$ tree pelican -L 2
pelican
├── README.md
├── content
│   ├── Caenorhabditis\ elegans
:   :
│   └── zebrafish
├── pelican-fh5co-marble-modified
│   ├── locale
│   ├── static
│   ├── templates
│   └── translation.sh
├── pelican-plugins-modified
│   ├── i18n_subsites
│   ├── ipynb
│   ├── neighbors
│   ├── render_math
│   └── tipue_search
├── pelicanconf.py
└── static!important
    ├── theme
    └── thumbnails
```