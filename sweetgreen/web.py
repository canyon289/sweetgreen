from bs4 import BeautifulSoup
import pandas as pd
import json
import requests
import ipdb 

LOCATIONS = ("Chicago", "Bay-Area", "new-york", "philadelpha",
              "boston", "dc-md-va", "los-angeles")

BASE_URL = "https://www.sweetgreen.com/menu/?region="

def parse_location(location=None):
    """Get list of menu items and ingredients per location"""
    file = open("menu_sweetgreen.html", "r")
    soup = BeautifulSoup(file.read(), 'html.parser')
    section_grids = soup.find_all(class_="section-grid")
    
    assert len(section_grids) == 4

    # Indices 0-3 are menu items
    all_menu_items = parse_menu_items(location, section_grids[:2])

    # Index 3 is the ingredients
    # ipdb.set_trace()
    all_ingredients = parse_ingredients(location, section_grids[3])
    return all_menu_items, all_ingredients


def parse_menu_items(location, menu_sections):
    """Parse all predefined menu items"""
    types = ("Seasonal", "WarmBowl", "Salad")
    all_menu_items = []

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
            
                all_menu_items.append({"location": location, "item_type":item_type,
                    "item_name":item_name, "calories":calories, "ingredients":ingredients})
    return all_menu_items


def parse_ingredients(location, menu_html):
    """Parse page to get ingredients list"""
    all_ingredients = []
    ingredient_types = ["bases", "ingredients", "premiums", "dressings"] 
    
    for ingredient_type in ingredient_types:
        ingredients_html = menu_html.find(id=ingredient_type).find_all(class_="ingredientlist")

        for ingredient_html in ingredients_html:
            ingredient_html = ingredient_html.find(class_="title")
            ingredient = ingredient_html.text

            try:
                seasonal = "32B593" in ingredient_html.attrs["style"]
            except:
                seasonal = False
            
            ingredient_json = {"location":location,
                    "ingredient_type":ingredient_type,
                    "ingredient":ingredient,
                    "seasonal":seasonal}

            all_ingredients.append(ingredient_json)
    return all_ingredients


def parse_locations(locations=None):
    """Parse all locations for menu items, ingredients, etc"""
    all_menu_items, all_ingredients = parse_location()

    for filename, obj in zip(("menu_items.json", "ingredients.json"), (all_menu_items, all_menu_items)):
        with open(filename, "w") as file_output:
            json.dump(obj, file_output, indent=4)
    return


def main():
    """Parse all webpages and output json"""
    parse_locations()
