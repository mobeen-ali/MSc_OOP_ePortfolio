"""
A utility module for basic arithmetic operations.
This module is part of a demonstration of packaging and testing in Python.
"""

class Calculator:
    """
    Calculator provides basic arithmetic operations.
    """

    def add(self, a, b):
        """Return the sum of two numbers."""
        return a + b

    def subtract(self, a, b):
        """Return the difference between two numbers."""
        return a - b

    def multiply(self, a, b):
        """Return the product of two numbers."""
        return a * b

    def divide(self, a, b):
        """
        Return the division result of two numbers.
        Raises ZeroDivisionError if b is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b
