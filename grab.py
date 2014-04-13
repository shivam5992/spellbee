import requests
import re
import mydic
import stopwords
import string
from BeautifulSoup import BeautifulSoup
from nltk import stem
from nltk.stem.wordnet import WordNetLemmatizer
import HTMLParser

def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title','noscript','link']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True

def get_text(url):
	r = requests.get(url)
	htmltext = r.text.encode("utf-8").decode("ascii","ignore")
	soup = BeautifulSoup(htmltext)		
	texts = soup.findAll(text=True)
	visible_texts = filter(visible, texts)
	article = ""
	for text in visible_texts:
		text = text.strip()
		if text:
			text = str(text.encode("utf-8").decode("ascii","ignore"))
			text += " "
			article += text
	article = str(HTMLParser.HTMLParser().unescape(article).encode("utf-8").decode("ascii","ignore"))
	return article

def mystemmer(word):
	worde = word
	if word.endswith("ied"):
		word = word.replace("ied","y")
	
	elif word.endswith("ed"):
		worde = word.replace("ed","e")
		word = word.rstrip("ed")
	
	elif word.endswith("ing"):
		worde = word.replace("ing","e")
		word = word.rstrip("ing")
	
	elif word.endswith("est"):
		worde = word.replace("est","e")
		word = word.rstrip("est")

	elif word.endswith("er"):
		word = word.rstrip("er")

	elif word.endswith("ment"):
		word = word.rstrip("ment")
		
	elif word.endswith("iest"):
		word = word.rstrip("iest")
	
	elif word.endswith("ies"):
		word = word.replace("ies","y")
	
	elif word.endswith("s"):
		word = word.rstrip("s")
	
	return word, worde

if __name__ == '__main__':
	url = "http://indianautosblog.com/2014/04/honda-mobilio-website-launched-127379"
	
	exclude = list(set(string.punctuation))
	snowball = stem.snowball.EnglishStemmer()
	lmtzr = WordNetLemmatizer()
	custom_list1 = open("data/verbs.txt").read().split("\n")
	custom_list2 = open("data/websitesandother.txt").read().split("\n")


	article = get_text(url)
	#article = open("data/random_text.txt").read()
	word_list = article.lower().split()

	possibles = []
	for word in word_list:
		flag = 0
		for spchar in exclude:
			word = word.rstrip(spchar).lstrip(spchar)
		if not re.search("\d+",word) and not word in stopwords.stopwords and len(word) > 3:
			for spchar in exclude:
 				if spchar in word:
 					flag = 1
 			if flag == 0:
 				try:
	 				if word in mydic.mydic:
						pass
					elif snowball.stem(word) in mydic.mydic:
						pass
					elif lmtzr.lemmatize(word) in mydic.mydic:
						pass
					elif mystemmer(word)[0] in mydic.mydic:
						pass
					elif mystemmer(word)[1] in mydic.mydic:
						pass
					elif word in custom_list1:
						pass
					elif word in custom_list2:
						pass
					else:
						possibles.append(word.strip())
				except:
					continue
					
	possibles = sorted(list(set(possibles)))
	for word in possibles:
		print word

''' LEFT NER'''
