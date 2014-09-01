'''
Name: Spell Corrector in Python
Version: 1.0

author: Shivam Bansal
author_email = shivam5992@gmail.com

'''

try:
	from nltk.stem.wordnet import WordNetLemmatizer
	from nltk import stem, pos_tag
	from Levenshtein import *
	from stopwords import stopwords
	from myWordNet import myWordNet
except ImportError as IE:
	print str(IE)

class SpellCheck():

	'''
    Main class for spell checking.
    '''

	def __init__(self):
		self.snowball = stem.snowball.EnglishStemmer()
		self.lmtzr = WordNetLemmatizer()
		self.max_error_length = 12
		self.max_suggestions = 10

	def _clean(self, text):
		''' 
		Cleans a text, handles decoding and encodings, html escaping etc.
		Third party package will be used in future versions.
		'''

		return str(text.strip())

	def _get_threshold(self, text):
		'''
		Decides the threshold for error limit in spellings, 
		depends on length of the word.
		'''

		if len(text) > 3:
			return 3
		else:
			return len(text)

	def _checkLevdis(self, query, listname, threshold, isDict):
		'''
		Checks the Levenshtein distance between query and db, 
		and returns the possible suggestions
		'''

		maxRatio = 0
		possibles = []
		closest = query

		if isDict:
			for each, value in listname:
				each = str(each)
				if distance(each, query) < threshold:
					WordRatio = ratio(each, query)
					if WordRatio > maxRatio:
						closest = value
						maxRatio = WordRatio
						possibles.append(value)

		else:
			for each in listname:
				each = str(each)
				if distance(each, query) < threshold:
					WordRatio = ratio(each, query)
					if WordRatio > maxRatio:
						closest = each
						maxRatio = WordRatio
						possibles.append(each)

		return closest, possibles, maxRatio

	def _correct(self, text):
		''' 
		Checks the input string and gives spelling suggestions as output
		
		:param str text: input text with spelling mistakes
		'''

		string = self._clean(text)
		words = string.split()

		suggestions = []
		for ind, query in enumerate(words):
			query = query.strip()

			if len(query) == 1:
				if query == 'i':
					suggestions.append(('I', []))
			elif len(query) < self.max_error_length:
				
				threshold = self._get_threshold(query)	
				query = query.lower()
				
				corrected = False
				if query in myWordNet:
				 	suggestions.append((myWordNet[query], []))
				 	corrected = True

				elif query in stopwords:
					suggestions.append((query, []))
				 	corrected = True

				else:
					closest, possibles, maxRatio = self._checkLevdis(query, stopwords, threshold, False)
					if maxRatio != 0:
						suggestions.append((closest, possibles[:self.max_suggestions][:-1]))
						corrected = True

			if corrected == False:
				closest, possibles, maxRatio = self._checkLevdis(query, myWordNet.iteritems(), threshold, True)
				if maxRatio != 0:
					suggestions.append((closest, possibles[:self.max_suggestions][:-1]))
					corrected = True

			if corrected == False:		
				for key, value in myWordNet.iteritems():
					if self.snowball.stem(query) in myWordNet:
						suggestions.append((value, []))
						corrected = True
					elif self.lmtzr.lemmatize(query) in myWordNet:
						suggestions.append((value, []))
						corrected = True
		return suggestions

if __name__ == '__main__':
	string = "This is my querye detectix0n tassk ahowever i donnt knoz whar to do"
	suggestions = SpellCheck()._correct(string)
	for x in suggestions:
		print x