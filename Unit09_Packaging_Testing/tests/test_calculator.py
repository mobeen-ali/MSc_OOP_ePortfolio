"""
Unit tests for the Calculator class in the math_utils module.
"""

import unittest
from math_utils.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)

    def test_divide(self):
        self.assertAlmostEqual(self.calc.divide(10, 2), 5.0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)


if __name__ == "__main__":
    unittest.main()
