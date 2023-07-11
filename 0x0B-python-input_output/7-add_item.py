tems to a list and save to a JSON file"""

import sys
import json
from os.path import exists
from typing import List


def save_to_json_file(my_obj: List[str], filename: str) -> None:
    """Save an object to a JSON file"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename: str) -> List[str]:
    """Load an object from a JSON file"""
    with open(filename, 'r') as file:
        return json.load(file)


def add_items_to_list(items: List[str]) -> None:
    """Add items to a list and save to a JSON file"""
    filename = "add_item.json"
    if exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(items)
    save_to_json_file(my_list, filename)


if __name__ == '__main__':
    args = sys.argv[1:]
    add_items_to_list(args)
