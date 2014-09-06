'''
Name: Spellbee
Description: Spelling Corrector in Python
Version: 1.0

author: Shivam Bansal
author_email = shivam5992@gmail.com

'''

try:
	from Levenshtein import *
	from lookups.stopwords import stopwords
	from lookups.myWordNet import myWordNet
except ImportError as IE:
	print str(IE)

class SpellCheck():

	'''
    Main class for spell checking.
    '''

	def __init__(self):
		self.max_error_length = 15
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

		if len(text) > 5:
			return 3
		elif len(text) > 3 and len(text) <= 5:
			return 2
		else:   
			return 1

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
				if len(each) < self.max_error_length:
					if distance(each, query) < threshold:
						WordRatio = ratio(each, query)
						if WordRatio > maxRatio:
							closest = value
							maxRatio = WordRatio
							possibles.append(value)

		else:
			for each in listname:
				each = str(each)
				if threshold == 1 and distance(each, query) <= threshold:
					closest = each
					possibles.append(each)
				elif distance(each, query) < threshold:
					WordRatio = ratio(each, query)
					if WordRatio > maxRatio:
						closest = each
						maxRatio = WordRatio
						possibles.append(each)

		return closest, possibles, maxRatio

	def _stopwordCheck(self, query, threshold):
		if query in stopwords:
			return (query, [])
		else:
			closest, possibles, maxRatio = self._checkLevdis(query, stopwords, threshold, False)
			if threshold == 1:
				if maxRatio == 0:
					return (closest, possibles[:self.max_suggestions][:-1]) 
			if maxRatio != 0:
				return (closest, possibles[:self.max_suggestions][:-1])
			else:
				return None

	def _correct(self, text):
		''' 
		Checks the input string and gives spelling suggestions as output
		
		:param str text: input text with spelling mistakes
		'''

		string = self._clean(text)
		words = string.split()

		suggestions = []
		for ind, query in enumerate(words):
			corrected = False
			query = query.strip()
			query = query.lower()

			
			if len(query) == 1:
				if query == 'i':
					suggestions.append(('I', []))
				else:
					suggestions.append((query, []))
				corrected = True
			

			elif len(query) == 2:
				res = self._stopwordCheck(query, 1)
				if res != None:
					suggestions.append(res)
					corrected = True
				else:
					corrected = False
					suggestions.append((query, []))


			elif len(query) < self.max_error_length:				
				threshold = self._get_threshold(query)	
				
				res = self._stopwordCheck(query, threshold)
				if res != None:
					suggestions.append(res)
				else:
					if query in myWordNet:
				 		suggestions.append((myWordNet[query], []))
				 		corrected = True

					if corrected == False:
						closest, possibles, maxRatio = self._checkLevdis(query, myWordNet.iteritems(), threshold, True)
						if maxRatio != 0:
							suggestions.append((closest, possibles[:self.max_suggestions][:-1]))
							corrected = True

						else:
							suggestions.append((query, []))

		return suggestions

spellbee = SpellCheck()










