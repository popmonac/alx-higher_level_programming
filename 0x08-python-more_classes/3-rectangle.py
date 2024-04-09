#!/usr/bin/python3
"""Module Rectangle"""


class Rectangle:
    """
    This Function create a Rectangle Class
    
    Attributes:
    width (int): Width of rectangle
    height (int): Height if rectangle
    """
    def __init__(self, height=0, width=0):
        """
            initializes the public attributes

            width (int): Width of the rectangle
            height (int): Height of the rectangle

            Return: Nothing
        """
        self.__height = height
        self.__width = width

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

            Attributes:
                value (int): The value of the height needed

            Returns: Nothing
        """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            Calculate the area of the rectangle

            Uses Class attributes

            Return: The area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
            Calculate the perimeter of the rectangle

            Uses Class attributes

            Return: The perimeter of the rectangle if height
                or width not equal to zero else return zero
        """
        if (self.__height == 0 or self.__width == 0):
            return (0)
        else:
            return (2 * (self.__width + self.__height))

    def __str__(self):
        """print the # according to the parameter given

        Returns:
            _type_: string
        """
        if (self.__height == 0 or self.__width == 0):
            return ("")
        return ((("#" * self.__width + "\n") * self.__height)[:-1])
