from Levenshtein import *
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import stem, pos_tag
from stopwords import stopwords
from mydic import mydic


snowball = stem.snowball.EnglishStemmer()
lmtzr = WordNetLemmatizer()

def similarity(text1, text2):
	text1 = sorted(text1)
	text2 = sorted(text2)
	print text1, text2

def corrector(text):
	print "Query: " + text
	print
	words = text.split()
	for query in words:
		print 
		query = query.lower()
		got = False

		if query in mydic:
		 	print query, ":" , mydic[query]
		 	got = True

		elif query in stopwords:
			print query, ":" , query
			got = True

		else:
			max_ratio = 0
			possibles = []
			for stop in stopwords:
				stop = str(stop)
				if distance(stop, query) < 3:
					rat = ratio(stop, query)
					if rat > max_ratio:
						closest = stop
						max_ratio_so_far = rat
						possibles.append(stop)
			if max_ratio != 0:
				print query, ":", closest, "(or " , ", ".join(possibles[:10][:-1]), ")"
				got = True


		
		if got == False:
			max_ratio_so_far = 0
			possibles = []
			for key, value in mydic.iteritems():
				key = str(key)
				if distance(key, query) < 3:
					rat = ratio(key, query)
					if rat > max_ratio_so_far:
						closest = value
						max_ratio_so_far = rat
						possibles.append(value)
			if max_ratio_so_far != 0:
				print query, ":", closest, "(or " , ", ".join(possibles[:10][:-1]), ")"
				got = True

		if got == False:		
			for key, value in mydic.iteritems():
				if snowball.stem(query) in mydic:
					print query, ":" ,value
					got = True
				elif lmtzr.lemmatize(query) in mydic:
					print query, ":" ,value
					got = True

corrector("This is my querye detectixon tassk ahowever i donnt knoz whar to do")