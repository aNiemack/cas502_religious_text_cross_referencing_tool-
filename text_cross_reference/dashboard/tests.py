from django.test import TestCase
import unittest
from views import highlight_searched

class TestHighlight(unittest.TestCase):
    def test_matches_are_marked_up(self):
        returnValue1 = highlight_searched("test", "this is a test")
        self.assertEqual(returnValue1, "this is a <mark>test</mark>")

        returnValue2 = highlight_searched("test", "this is a test this is a test")
        self.assertEqual(returnValue2, "this is a <mark>test</mark> this is a <mark>test</mark>")

    def test_empty_search(self):
        returnValue = highlight_searched("", "this is a test")
        self.assertEqual(returnValue, "this is a test")

    def test_empty_text(self):
        returnValue = highlight_searched("", "")
        self.assertEqual(returnValue, "")

    def test_capitalization(self):
        returnValue1 = highlight_searched("test", "this is a Test")
        self.assertEqual(returnValue1, "this is a <mark>Test</mark>")

        returnValue2 = highlight_searched("TeSt", "this is a Test")
        self.assertEqual(returnValue2, "this is a <mark>Test</mark>")
