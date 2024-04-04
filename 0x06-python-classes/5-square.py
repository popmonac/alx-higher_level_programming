#!/usr/bin/python3
"""Module Sqaure"""

class Square:
    """ Square class defined by geometric shap

         Attributes:
            size (int): Size of the square
    """

    def __init__(self, size):
        """initializes the square
         Args:
            size (int): size of the square

            Returns:
            None
        """
        self.size = size

    @property
    def size(self):
        """
            Setter of size

            Args:
                size (int): size of the square
            Raises
                TypeError: if size is not int
                ValueError: size less than 0
            Returns:
                None
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")