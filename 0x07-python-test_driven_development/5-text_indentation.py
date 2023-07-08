#!/usr/bin/python3
# 4-print_square.py
"""
Module: 5-text_indentation

Description:
This module defines a function that prints a text with 2 new lines after each of these characters: ., ? and :.

"""


def text_indentation(text):
    """
    Prints the text with 2 new lines after each occurrence of ., ? and : characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = [".", "?", ":"]
    result = ""
    for char in text:
        result += char
        if char in chars:
            result += "\n\n"

    print("\n".join(line.strip() for line in result.split("\n")))
