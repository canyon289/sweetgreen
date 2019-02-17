"""
Cleans raw JSON files and turns them into dataframes
"""
import os
from .utils import read_json, write_json


FILE_PATH_RAW = os.getenv("file_path", os.path.join("data", "raw"))
FILE_PATH_CLEAN = os.getenv("file_path", os.path.join("data", "cleaned"))
MENU_RAW_JSON = os.getenv("raw_menu_json", "raw_menu_items.json")
INGREDIENTS_RAW_JSON = os.getenv("raw_ingredients", "raw_ingredients.json")


def clean_ingredients(file_path, file_name):
    """Clean ingredients JSON file"""

    full_file_path = os.path.join(file_path, file_name)
    raw_ingredients_json = read_json(full_file_path)

    for ingredient in raw_ingredients_json:
        ingredient["ingredient"] = ingredient["ingredient"].strip().lower()

    write_json(file_path, "cleaned_ingredients.json")
    return


def clean_raw_files():
    clean_ingredients(FILE_PATH_RAW, INGREDIENTS_RAW_JSON)
    return
