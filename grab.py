import requests, re, pprint, mydic
from BeautifulSoup import BeautifulSoup
from nltk import stem
from nltk.stem.wordnet import WordNetLemmatizer
stopwords = ["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title','noscript','link']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True
url = "http://stackoverflow.com/questions/771918/how-do-i-do-word-stemming-or-lemmatization"
r = requests.get(url)
htmltext = r.text.encode("utf-8").decode("ascii","ignore")
soup = BeautifulSoup(htmltext)		
texts = soup.findAll(text=True)
visible_texts = filter(visible, texts)
article = ""
for text in visible_texts:
	text = text.strip()
	if text:
		text += " "
		article += text.encode("utf-8")
article = str(article)
article = str(BeautifulSoup(article, convertEntities=BeautifulSoup.HTML_ENTITIES))
word_list = article.lower().split()
wl = []
for w in word_list:
	w = w.lstrip(",").rstrip(",").rstrip(".").lstrip(".").lstrip("(").rstrip(")").lstrip("!").rstrip("!").strip()
	if w:
		wl.append(w)
wl = sorted(list(set(wl)))
snowball = stem.snowball.EnglishStemmer()
lmtzr = WordNetLemmatizer()
for w in wl:
	if not w in stopwords and not w.isdigit():
		if w in mydic.mydic:
			pass
		elif snowball.stem(w) in mydic.mydic:
			pass
		elif lmtzr.lemmatize(w) in mydic.mydic:
			pass
		elif w.replace("ed","e") in mydic.mydic:
			pass
		elif w.replace("ing"," ").strip() in mydic.mydic:
			pass
		else:
			print w
			


