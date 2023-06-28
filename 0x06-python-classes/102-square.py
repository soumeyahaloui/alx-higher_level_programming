#!/usr/bin/python3

"""Define a class Square that defines a square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (float or int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __lt__(self, other):
        """Check if the area of the square is less than the other square's area.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area of the square is less than the other square's area, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Check if the area of the square is less than or equal to the other square's area.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area of the square is less than or equal to the other square's area, False otherwise.
        """
        return self.area() <= other.area()

    def __eq__(self, other):
        """Check if the area of the square is equal to the other square's area.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area of the square is equal to the other square's area, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if the area of the square is not equal to the other square's area.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area of the square is not equal to the other square's area, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """Check if the area of the square is greater than the other square's area.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area of the square is greater than the other square's area, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if the area of the square is greater than or equal to the other square's area.

        Args:
            other (Square): The other square to compare with.

        Returns:
            bool: True if the area of the square is greater than or equal to the other square's area, False otherwise.
        """
        return self.area() >= other.area()
