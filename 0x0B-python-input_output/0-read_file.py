#!/usr/bin/python3
"""The Function For file manipulation"""


def read_file(filename=""):
    """This Function reads from a file"""

    with open(filename, 'r', encoding='utf-8') as file:

        content = file.read()

        print(content, end="")
