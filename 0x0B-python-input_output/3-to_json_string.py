#!/usr/bin/python3
""""This function deals with Json"""
import json


def to_json_string(my_obj):
    """
    Function that returns the Json representation of an object.
    """
    return json.dumps(my_obj)
