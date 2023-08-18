#!/usr/bin/python3

"""
Module: 3-say_my_name

Description:
This module defines a function that prints a name.

"""


def say_my_name(first_name, last_name=""):
    """
    Prints the name in the format "My name is <first name> <last name>".

    Args:
        first_name (str): The first name.
        last_name (str): The last name. Default value is an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
