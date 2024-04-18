#!/usr/bin/python3
"""This funtion deals with Json"""
import json


def save_to_json_file(my_obj, filename):

    """Funtion writes an object to a text file"""

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
