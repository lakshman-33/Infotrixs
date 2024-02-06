import unittest
from io import StringIO
import sys
import word_manipulator  # Assuming the main script is saved as "word_manipulation.py"

class TestWordManipulation(unittest.TestCase):
    def test_count_occurrences(self):
        text = "This is a test. This test is simple."
        count = word_manipulator.count_word_occurrences(text, "test")
        self.assertEqual(count, 2)
    
    def test_replace_word(self):
        text = "Hello, world!"
        new_text = word_manipulator.replace_word(text, "world", "Python")
        self.assertEqual(new_text, "Hello, Python!")

if __name__== "__main__":
    unittest.main()