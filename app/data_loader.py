import json
import os

def load_projects(path="portfolio.json"):
    base_dir = os.path.dirname(__file__)  # Gets the directory of data_loader.py
    file_path = os.path.join(base_dir, path)
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
