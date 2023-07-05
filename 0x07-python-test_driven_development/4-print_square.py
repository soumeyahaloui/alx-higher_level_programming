#!/usr/bin/python3

"""
Module: 4-print_square

Description:
This module defines a function that prints a square with the character #.

"""


def print_square(size):
    """
    Prints a square of size `size` with the character #.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer or a float.
        ValueError: If size is less than 0.
        TypeError: If size is a float and less than 0.

    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
