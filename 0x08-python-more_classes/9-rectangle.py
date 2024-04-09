#!/usr/bin/python3
"""Module Rectangle"""


class Rectangle:
    """Rectangle Class

    Raises:
        TypeError: width must be an integer
        ValueError: width must be >= 0
        TypeError: width must be an integer
        ValueError: width must be >= 0
        TypeError: width must be an integer
        TypeError: width must be an integer

    Returns:
        Rectangle: Rectangle made is type of char or string
        but default is #
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, height=0, width=0):
        """Initialzes the class

        Args:
            width (int, optional): Parameters needed. Defaults to 0.
            height (int, optional): Parameters needed. Defaults to 0.
        """
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Method that returns the width

        Returns:
            (int): self.__width (The width of the retangle)
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ set the width needed

        Args:
            value (int): integer needed

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Method that returns the height

        Returns:
            (int): self.__height (The height of the retangle)
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ set the height needed

        Args:
            value (int): integer needed

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
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
            string: The string on Success and ("" on Failure)
        """
        if (self.__height == 0 or self.__width == 0):
            return ("")
        rectangle = str(self.print_symbol)
        return (((rectangle * self.__width + "\n") * self.__height)[:-1])

    def __repr__(self):
        """Gets the reprentation of the string

        Returns:
            string: The string passed
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Delete instances when needed
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """_summary_

        Args:
            rect_1 (Rectangle): rectangle create by instances
            rect_2 (Rectangle): rectangle create by instances

        Raises:
            TypeError: rect_1 must be an instance of Rectangle
            TypeError: rect_1 must be an instance of Rectangle

        Returns:
            Rectangle: If the instances returns true it returns
            one of the rectangle
        """
        if not (isinstance(rect_1, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not (isinstance(rect_2, Rectangle)):
            raise TypeError("rect_1 must be an instance of Rectangle")
        Area_1 = rect_1.area()
        Area_2 = rect_2.area()
        if Area_1 >= Area_2:
            return rect_1
        else:
            rect_2

    @classmethod
    def square(cls, size=0):
        """
        Creates a new Rectangle instance with equal width and height

        Args:
            cls (class): The class itself.
            size (int): The size to set for both width and height

        Returns:
            Rectangle: A new Rectangle instance with equal width and height.
        """
        return (cls(size, size))
