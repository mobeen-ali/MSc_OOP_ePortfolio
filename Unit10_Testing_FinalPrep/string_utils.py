"""
string_utils.py

A simple utility module for string manipulation.
Includes functions to reverse strings, count vowels, and format titles.
"""

def reverse_string(text):
    """
    Return the reverse of the input string.

    Args:
        text (str): Input string to reverse.

    Returns:
        str: Reversed string.
    """
    return text[::-1]


def count_vowels(text):
    """
    Count the number of vowels in the string.

    Args:
        text (str): Input string.

    Returns:
        int: Total number of vowels found.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def format_title(text):
    """
    Capitalize each word in the string like a title.

    Args:
        text (str): Input string.

    Returns:
        str: Title-cased string.
    """
    return text.title()
