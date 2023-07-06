#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter/setter for the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle.

        Args:
            value (int): The width value.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter/setter for the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle.

        Args:
            value (int): The height value.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the Rectangle.

        Returns:
            int: The calculated area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the Rectangle.

        Returns:
            int: The calculated perimeter.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
