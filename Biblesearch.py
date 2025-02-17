def word_search(word):
	count = 0
	with open('EnglishESVBible.xml', 'r') as f:
		for line in f:
			words = line.split()
			for i in words:
				if(i.lower()==word):
					count=count+1
	return count


