"""
Utility Functions
"""
import json


def write_json(filename, obj):
    """Dump JSON to disk"""
    with open(filename, "w") as file_output:
        json.dump(obj, file_output, indent=4)
    return
