#!/usr/bin/python3
"""Module Square"""

class Square:
    """Defines an instance of a square"""

    def __init__(self, size=0):

        """initializes the square
        Args:
            size (int): size of the square

        Returns:
            None
        """
        
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
