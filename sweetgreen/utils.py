"""
Utility Functions
"""
import json
import os
import glob


def write_json(file_path, file_name, obj):
    """Dump JSON to disk"""
    full_file_path = os.path.join(file_path, file_name)
    with open(full_file_path, "w") as file_output:
        json.dump(obj, file_output, indent=4)
    return


def read_json(file_name, file_path=None):
    """Read file from json. Specify file_path optionally"""
    if file_path:
        file_name = os.path.join(file_path, file_name)

    with open(file_name, "r") as file_input:
        return json.load(file_input)


def load_all_restaurant_menus(file_path):
    """Loads all json files from one directory into an array"""
    glob_string = "{}/{}".format(file_path, "*.json")
    json_paths = glob.iglob(glob_string)

    jsons = [read_json(json_path) for json_path in json_paths]

    return jsons
