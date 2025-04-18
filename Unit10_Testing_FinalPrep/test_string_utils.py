"""
Unit tests for the string_utils module.
"""

import unittest
import string_utils


class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(string_utils.reverse_string("hello"), "olleh")
        self.assertEqual(string_utils.reverse_string(""), "")

    def test_count_vowels(self):
        self.assertEqual(string_utils.count_vowels("education"), 5)
        self.assertEqual(string_utils.count_vowels("xyz"), 0)

    def test_format_title(self):
        self.assertEqual(string_utils.format_title("hello world"), "Hello World")
        self.assertEqual(string_utils.format_title("mobeen ali"), "Mobeen Ali")


if __name__ == "__main__":
    unittest.main()
