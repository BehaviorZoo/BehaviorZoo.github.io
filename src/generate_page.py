# coding-utf:8
import os
import re
import argparse
import numpy as np
import pandas as pd
from pycharmers.utils import str_strip, toBLUE, toGREEN
from jinja2 import Environment, FileSystemLoader

here = os.path.abspath(os.path.dirname(__file__))
templates_dir   = os.path.join(here, "templates")
default_out_dir = os.path.join(here, "../pelican/content")
env = Environment(loader=FileSystemLoader(templates_dir))

colnames     = ["ID", "PIC", "status", "animal", "species", "Title", "Author", "Journal", "yyyymmdd", "Year", "vol_num_page", "URL", "DOI", "dataset_type", "dataset_url", "code", "size", "quality", "field_lab", "dimension", "Tracking_method", "tag1", "tag2", "tag3", "tag4", "notes"]
tag_colnames = ["tag1", "tag2", "tag3", "tag4", "Journal"]

def _makedirs(name, mode=511, msg=""):
    if not os.path.exists(name):
        os.makedirs(name=name, mode=mode)
        print(f"{toBLUE(name)} is created. {msg}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="generate_page", add_help=True)
    parser.add_argument("-D", "--data",          type=str, required=True,           help="Path to data.")
    parser.add_argument("-O", "--out-dir",       type=str, default=default_out_dir, help="Path to output directory name.")
    parser.add_argument("-T", "--template-name", type=str, default="simple.tpl",    help=f"Path to template file from {templates_dir}.")
    args = parser.parse_args()

    data_path     = args.data
    out_dir       = args.out_dir
    template_name = args.template_name
    _makedirs(name=out_dir)

    data = pd.read_excel(io=data_path).head(33).values
    template = env.get_template(name=template_name)

    idx = 0
    for i,row_data in enumerate(data):
        row_data = dict(zip(colnames, row_data))
        # Title
        row_data["Title"] = str_strip(str(row_data.get("Title")))
        # Tags
        row_data["Tags"] = ", ".join([row_data.get(e) for e in tag_colnames if isinstance(row_data.get(e), str) or not np.isnan(row_data.get(e))])
        # yyyymmdd
        default_yyyymmdd = "1111-11-11"
        yyyymmdd = row_data.get("yyyymmdd", default_yyyymmdd)
        if not np.isnan(yyyymmdd):
            yyyymmdd = str(int(yyyymmdd)) 
            if len(yyyymmdd) < 8:
                yyyymmdd += "01"
            yyyymmdd = f"{yyyymmdd[:4]}-{yyyymmdd[4:6]}-{yyyymmdd[6:]}"
        else:
            yyyymmdd = default_yyyymmdd
        row_data["yyyymmdd"] = yyyymmdd

        # Animal
        default_animal = "others"
        animal = row_data.get("animal", default_animal)
        if not isinstance(animal, str):
            animal = default_animal
        for category in animal.split(","):
            idx += 1
            category_dir = os.path.join(out_dir, str_strip(category))
            row_data["animal"] = category
            row_data["idx"] = idx
            _makedirs(name=category_dir)
            article_fn = os.path.join(category_dir, f"{idx}.md")
            with open(article_fn, mode="w") as f:
                print(f"\t{toGREEN(article_fn)} is generated.")
                f.write(template.render(row_data))
