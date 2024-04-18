#!/usr/bin/python3
"""This funtion deals with Json"""
import json


def load_from_json_file(filename):
    """This function that creates an Object from a “JSON file”"""

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()

    return (json.loads(content))
