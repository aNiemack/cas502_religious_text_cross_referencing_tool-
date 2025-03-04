import unittest
import Biblesearch

class TestWord_Search(unittest.TestCase):
	
	def test_wordsearch_word_that_exists(self):
		Count = Biblesearch.word_search("heaven")
		self.assertEqual(Count, 242)		

	def test_wordsearch_no_return(self):
		Count = Biblesearch.word_search("computer")
		self.assertEqual(Count, 0)

	def test_wordsearch_no_input(self):
		Count = Biblesearch.word_search("")
		self.assertEqual(Count, 0)	

# The challenges I faced when writing these tests were 
# that I did not understand initially how the values worked
# to test the function that I wanted to write. Another 
# challenge was in writing the actual code that this test 
# was meant to test. I figured out how to do grep, but I 
# had a lot of difficulty translating that into python.

