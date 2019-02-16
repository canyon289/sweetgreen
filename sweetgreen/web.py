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
    section = section_grids[0]

    all_menu_items = []

    # Indices 0-3 are menu items
    types = ("Seasonal", "WarmBowl", "Salad")
    for item_type, menu_html in zip(types, section_grids[:2]):
        menu_items = parse_menu_items(location, item_type, menu_html)
        all_menu_items.extend(menu_items)

    # Index 4 is the ingredients
    # ipdb.set_trace()
    return all_menu_items


def parse_menu_items(location, item_type, menu_html):
    """Parse all predefined menu items"""
    menu_items = []
    raw_menu_items = menu_html.find_all(class_="cols pad")
    
    assert len(raw_menu_items) > 0

    for raw_menu_item in raw_menu_items:
        calories_html = raw_menu_item.find(class_="callories")
        
        # Only menu items have a callories child elements
        if calories_html is not None:
            calories = calories_html.text
            item_name = raw_menu_item.find("h2").text
            ingredients = raw_menu_item.find("p").text
        
            menu_items.append({"location": location, "item_type":item_type,
                "item_name":item_name, "calories":calories, "ingredients":ingredients})
    return menu_items


def parse_ingredients():
    return


def parse_locations(locations=None):
    """Parse all locations for menu items, ingredients, etc"""
    all_menu_items = parse_location()

    with open("menu_items.json", "w") as menu_output:
        json.dump(all_menu_items, menu_output, indent=4)
    return


def main():
    """Parse all webpages and output json"""
    parse_locations()
