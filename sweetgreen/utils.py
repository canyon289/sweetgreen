"""
Utility Functions
"""
import json
import os


def write_json(file_path, file_name, obj):
    """Dump JSON to disk"""
    full_file_path = os.path.join(file_path, file_name)
    with open(full_file_path, "w") as file_output:
        json.dump(obj, file_output, indent=4)
    return


def read_json(file_name, file_path):
    full_file_path = os.path.join(file_path, file_name)
    with open(full_file_path, "r") as file_input:
        return json.load(file_input)
