#!/usr/bin/python3
"""This funtion deals with Json"""
import json


def from_json_string(my_str):
    """This Funtion returns the Python data structure
        represented by a Json string.
    """
    return json.loads(my_str)
