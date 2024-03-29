"""
Cleans raw JSON files and turns them into dataframes
"""
import os
import json

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

        # Move asset ID up
        for ingredient in ingredients_jsons:
            try:
                assert len(ingredient["asset_ids"]) == 1
            except AssertionError:
                # Some ingredients have multiple assets
                if ingredient["short"] in ("balsamic squash",):
                    pass

            ingredient["asset_ids"] = ingredient["asset_ids"][0]

        compiled_ingredients = utils.compile_jsons(
            ingredients_jsons, "id", compiled_ingredients
        )

    utils.write_json(output_file_path, output_file_name, compiled_ingredients)
    return


def compile_ingredients_per_restaurant():
    """Goes through JSON and creates json of restaurant with all ingredients"""
    raise NotImplementedError


def flatten_restaurants_json(
    raw_file_path=RAW_FILE_PATH,
    raw_file_name="raw_restaurants.json",
    output_file_path=FILE_PATH_CLEAN,
    output_file_name="flattened_restaurants.json",
):
    """Flattens restaurant JSON to make it easier to load into a Pandas Dataframe"""
    logger.info("Flattening restaurants from raw restaurant json")

    raw_restaurant_json = utils.read_json(os.path.join(raw_file_path, raw_file_name))

    raw_restaurants = raw_restaurant_json["restaurants"]

    for restaurant in raw_restaurants:
        for key in (
            "available_dropoff_locations",
            "dietary_preference_overrides",
            "asset_ids",
        ):
            restaurant[key] = json.dumps(restaurant[key])

        hours = restaurant.pop("hours")

        # Flatten days open
        possible_days = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"}
        for day in hours:
            try:
                day_str = day["wday"]
                possible_days.remove(day_str)
                restaurant[f"{day_str}_start"] = day["start"]
                restaurant[f"{day_str}_end"] = day["end"]

            except (TypeError, KeyError):
                pass

        for possible_day in possible_days:
            restaurant[f"{possible_day}_start"] = None
            restaurant[f"{possible_day}_end"] = None

    utils.write_json(output_file_path, output_file_name, raw_restaurants)
    return


def compile_assets(
    raw_file_path=RAW_FILE_PATH,
    restaurant_menu_directory=SWEETGREEN_RESTAURANT_MENU_DIRECTORY,
    output_file_path=FILE_PATH_CLEAN,
    output_file_name="compiled_assets.json",
):
    """Compiles assets across restaurants"""
    logger.info("Compiling assets from all restaurant menus")

    restaurant_jsons = utils.load_all_json_directory(
        os.path.join(raw_file_path, restaurant_menu_directory)
    )

    compiled_assets = {}

    for restaurant_json in restaurant_jsons:
        assets = restaurant_json["assets"]

        # Drop Child IDs and get metadata
        metadatas = []
        for asset in assets:
            asset.pop("child_asset_ids", None)
            asset["metadata"] = json.dumps(asset["metadata"])

        # Create a dictionary of assets
        compiled_assets = utils.compile_jsons(assets, "id", compiled_assets)

    utils.write_json(output_file_path, output_file_name, compiled_assets)
    return


def index_products_by_restaurant(
    raw_file_path=RAW_FILE_PATH,
    restaurant_menu_directory=SWEETGREEN_RESTAURANT_MENU_DIRECTORY,
    output_file_path=FILE_PATH_CLEAN,
    output_file_name="indexed_restaurant_products.json",
):
    """Compiles products across restaurants.

    Notes
    -----
    Products can't be directly combined because restaurant and product properties are mixed
    in API return object. Rather than remove elements this file will be indexed by restaurant
    and left a bit more raw than usual for additional flexibility for EDA
    """
    logger.info("Indexing products from all restaurant menus")

    restaurant_jsons = utils.load_all_json_directory(
        os.path.join(raw_file_path, restaurant_menu_directory)
    )

    restaurant_product_index = {}
    for restaurant_json in restaurant_jsons:
        products = restaurant_json["products"]
        restaurant_id = products[0]["restaurant_id"]

        # Move asset ID up
        for product in products:
            assert len(product["asset_ids"]) == 1
            product["asset_ids"] = product["asset_ids"][0]

        restaurant_product_index[restaurant_id] = products

    utils.write_json(output_file_path, output_file_name, restaurant_product_index)
