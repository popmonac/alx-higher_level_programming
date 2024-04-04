#!/usr/bin/python3
"""Module square"""

class Square:
    """ Square class defined by geometric shap

                Attributes:
                    size (int): Size of the square
            """
    def __init__(self, size=0):
        """initializes the square
            Args:
                size (int): size of the square

            Returns:
                None
            """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        set square area

            Return:
                The current area (int)
            """ 
        return (self.__size * self.__size)