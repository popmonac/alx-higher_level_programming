#!/usr/bin/python3
"""Module Rectangle"""


class Rectangle:
    """
    This Function create a Rectangle Class

    Attributes:
        width (int): Width of rectangle
        height (int): Height if rectangle
    """
    def __init__(self, width=0, height=0):
        """
            initializes the public attributes

            width (int): Width of the rectangle
            height (int): Height of the rectangle

            Return: Nothing
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
            Retrives width

            Return: self.__width (The width of the retangle)
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
            Sets the width

            Attrinbutes:
                value (int): The value of the width needed

            Returns: Nothing
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            Retrives height

            Return: self.__height (The height of the retangle)
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
            Sets the height

            Attrinbutes:
                value (int): The value of the height needed

            Returns: Nothing
        """

        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
