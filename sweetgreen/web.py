from bs4 import BeautifulSoup
import requests
import os
import time
import random

from .utils import write_json

LOCATIONS = (
    "Chicago",
    "Bay-Area",
    "new-york",
    "philadelpha",
    "boston",
    "dc-md-va",
    "los-angeles",
)

WP_MENU_BASE_URL = "https://www.sweetgreen.com/menu/?region="
SWEETGREEN_RESTAURANT_LOCATION_BASE_URL = "https://order.sweetgreen.com/api/restaurants"


USER_AGENT_STRING = {'User-Agent':("Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-en) AppleWebKit/533.19.4"
                    " KHTML, like Gecko) Version/5.0.3 Safari/533.19.4")}

RAW_FILE_PATH = os.path.join("data", "raw")


def http_get(*args, **kwargs):
    """Make requests with some delay not to overload sweetgreens servers"""
    response = requests.get(*args, **kwargs)
    time.sleep(random.random()*2)
    return response


def parse_locations(base_url, locations=None):
    """Get list of menu items and ingredients per location"""
    all_ingredients = []
    all_menu_items = []
    for location in locations:
        print("Requesting HTML for {}".format(location))

        # Request HTML from web
        location_response = http_get(base_url, headers=USER_AGENT_STRING,
                                         params={"region": location})
        location_html = location_response.text

        # Parse HTML
        soup = BeautifulSoup(location_html, "html.parser")
        section_grids = soup.find_all(class_="section-grid")
        assert len(section_grids) == 4

        # Indices 0-2 are menu items
        region_menu_items = parse_menu_items(location, section_grids[:2])

        # Index 3 is the ingredients
        region_ingredients_items = parse_ingredients(location, section_grids[3])

        all_menu_items.extend(region_menu_items)
        all_ingredients.extend(region_ingredients_items)

    return all_menu_items, all_ingredients


def parse_menu_items(location, menu_sections):
    """Parse all predefined menu items"""
    types = ("Seasonal", "WarmBowl", "Salad")
    region_menu_items = []

    for item_type, menu_html in zip(types, menu_sections):

        raw_menu_items = menu_html.find_all(class_="cols pad")
        assert len(raw_menu_items) > 0
        for raw_menu_item in raw_menu_items:
            calories_html = raw_menu_item.find(class_="callories")

            # Only menu items have a callories child elements
            if calories_html is not None:
                calories = calories_html.text
                item_name = raw_menu_item.find("h2").text
                ingredients = raw_menu_item.find("p").text

                region_menu_items.append(
                    {
                        "location": location,
                        "item_type": item_type,
                        "item_name": item_name,
                        "calories": calories,
                        "ingredients": ingredients,
                    }
                )
    return region_menu_items


def parse_ingredients(location, menu_html):
    """Parse page to get ingredients list"""
    region_ingredients = []
    ingredient_types = ["bases", "ingredients", "premiums", "dressings"]

    for ingredient_type in ingredient_types:
        ingredients_html = menu_html.find(id=ingredient_type).find_all(
            class_="ingredientlist"
        )

        for ingredient_html in ingredients_html:
            ingredient_html = ingredient_html.find(class_="title")
            ingredient = ingredient_html.text

            try:
                seasonal = "32B593" in ingredient_html.attrs["style"]

            except KeyError:
                seasonal = False

            ingredient_json = {
                "location": location,
                "ingredient_type": ingredient_type,
                "ingredient": ingredient,
                "seasonal": seasonal,
            }

            region_ingredients.append(ingredient_json)
    return region_ingredients


def cache_sweetgreen_wordpress_content(file_path=RAW_FILE_PATH):
    """Parse all webpages and output json"""
    all_menu_items, all_ingredients = parse_locations(WP_MENU_BASE_URL, LOCATIONS)
    write_json(file_path, "raw_menu_items.json", all_menu_items)
    write_json(file_path, "raw_ingredients.json", all_ingredients)
    return


def cache_restaurants(restaurant_base_url=SWEETGREEN_RESTAURANT_LOCATION_BASE_URL,
                      pages=1,
                      per=1000):
    """Caches all available restaurant locations from sweetgreens ordering app"""
    print("Getting restaurant and outpost list from Sweetgreen")
    restaurant_response = http_get(restaurant_base_url, headers=USER_AGENT_STRING,
                                       params={"pages": pages, "per": per})

    restaurant_json = restaurant_response.json()
    write_json(RAW_FILE_PATH, "raw_restaurants.json", restaurant_json)
    return



