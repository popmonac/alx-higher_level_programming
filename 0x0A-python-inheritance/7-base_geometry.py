#!/usr/bin/python3
"""A Class Module"""


class BaseGeometry:
    """BaseGeometry Class"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """interger validator

        Args:
            name (string): info needed
            value (string): info needed

        Raises:
            TypeError: must be an integer
            ValueError: must be greater than
        """
        if (type(value)) == int:
            raise TypeError("{} must be an integer".format(name))
        if (value < 0):
            raise ValueError("{} must be greater than 0".format(name))
