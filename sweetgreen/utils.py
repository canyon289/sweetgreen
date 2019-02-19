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


def load_all_json_directory(file_path):
    """Loads all json files from one directory into an array"""
    glob_string = "{}/{}".format(file_path, "*.json")
    json_paths = glob.iglob(glob_string)

    jsons = [read_json(json_path) for json_path in json_paths]

    return jsons


def compile_jsons(json_array, key_name, input_json=None):
    """Given an array of JSON objects deduplicate lists, and verify consistency across arrays

    Parameters
    ----------
    json_array: list
        An array of json objects that could potentially be combined
    key_name: obj
        Key value of json
    input_json: dict, opt
        Existing store of json values

    Returns
    -------
    input_json: dict
        input_json with objects added from json_array

    """
    if input_json is None:
        input_json = {}

    # Iterate through json_array to combine with input_json
    for proposed_insert in json_array:

        # Get key of current json_value
        proposed_insert_id = proposed_insert[key_name]

        # Determine if there is an existing record with the same id
        existing_record = input_json.get(proposed_insert_id)

        if not existing_record:
            # No existing record, add immediately
            input_json[proposed_insert_id] = proposed_insert

        # Compare values to ensure everything is the same
        else:

            existing_record_str = json.dumps(existing_record, sort_keys=True)
            proposed_insert_str = json.dumps(proposed_insert, sort_keys=True)
            assert proposed_insert_str == existing_record_str

    return input_json
