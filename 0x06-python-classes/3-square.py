#!/usr/bin/python3
"""Module square"""

class Square:
    """ Square class defined by geometric shap

            Attributes:
                size (int): Size of the square
        """
    def __init__(self, size=0):
        
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    
    def area(self):
        """
        set square area

        Return:
            The current area (int)
        """
        return self.__size**2