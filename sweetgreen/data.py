"""
Cleans raw JSON files and turns them into dataframes
"""
import os

from . import getLogger

from . import utils
from .web import RAW_FILE_PATH, SWEETGREEN_RESTAURANT_MENU_DIRECTORY


FILE_PATH_CLEAN = os.getenv("file_path", os.path.join("data", "cleaned"))
MENU_RAW_JSON = os.getenv("raw_menu_json", "raw_menu_items.json")

logger = getLogger()


def clean_ingredients_web_scrape(
    file_path=FILE_PATH_CLEAN, file_name="cleaned_web_scraped_ingredients.json"
):
    """Clean web scraped ingredients"""

    full_file_path = os.path.join(file_path, file_name)
    raw_ingredients_json = utils.read_json(full_file_path)

    for ingredient in raw_ingredients_json:
        ingredient["ingredient"] = ingredient["ingredient"].strip().lower()

    utils.write_json(file_path, file_name)
    return


def compile_ingredients_json(
    raw_file_path=RAW_FILE_PATH,
    restaurant_menu_directory=SWEETGREEN_RESTAURANT_MENU_DIRECTORY,
    output_file_path=FILE_PATH_CLEAN,
    output_file_name="compiled_ingredients.json",
):
    """Iterate through restaurant JSONs and get list of ingredients and properties"""
    logger.info("Compiling ingredients from all restaurant menus")
    restaurant_jsons = utils.load_all_json_directory(
        os.path.join(raw_file_path, restaurant_menu_directory)
    )

    compiled_ingredients = {}
    for restaurant_json in restaurant_jsons:
        ingredients_jsons = restaurant_json["ingredients"]

        compiled_ingredients = utils.compile_jsons(
            ingredients_jsons, "id", compiled_ingredients
        )

    utils.write_json(output_file_path, output_file_name, compiled_ingredients)
    return


def flatten_restaurants_json(
        raw_file_path=RAW_FILE_PATH,
        raw_file_name="raw_restaurants.json",
        output_file_path=FILE_PATH_CLEAN,
        output_file_name="flattened_restaurants.json",
):
    """Flattens restaurant JSON to make it easier to load into a Pandas Dataframe"""

    raw_restaurant_json = utils.load_all_json_directory(
        os.path.join(raw_file_path, raw_file_name)
    )

    raw_restaurants = raw_restaurant_json["restaurant"]

    for restaurant in raw_restaurants:
        for key in ("available_dropoff_locations", "dietary_preference_overrides", "asset_ids"):
            restaurant[key] = str(key)

        hours = restaurant.pop("hours")
        for day in hours:
            day_str = day["wday"]
            restaurant[f"start_{day_str}"] = day["start"]
            restaurant[f"end_{day_str}"] = day["end"]
