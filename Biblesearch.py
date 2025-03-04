# This is a word search function that will search for string patterns within the EnglishESV Bible database. 
# Make sure EnglishESVBible.xml database is imported

def word_search(word):
	count = 0
	with open('EnglishESVBible.xml', 'r') as f:  
		for line in f:
			words = line.split()
			for i in words:
				if(i.lower()==word):
					count=count+1
	return count

# Current code does not return only the string input, but also identifies words that contain the string input

