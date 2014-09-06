Spellbee
---


Spellbee is an english spelling corrector and suggestor. It uses standard nlp tasks to achieve a better accuraccy level in terms of suggestions and corrections. Every query term undergoes a set of hierarichial well written rules. Queries are checked against various standardised lookup tables and dictionaries. If terms are not found in the tables, then most similar words are shown as spelling suggestions.

**Standardised LookUps:** Standardised lookup tables are created by processing the wordnet database which involves processes like stemming, lemmatization, stopword removal, tokenization, normalization, encoding handling, html unescaping. Wordnet database provides list of all possible words(almost) of english language, though they are not standardised hence needs to be processd once.

**Word Similarity:** It uses weighted edit distance (levenshtien) algorithm to find out number of operations required to change one word to another. To get most similar single word, word similarity ratio is calculated. The one with maximum ratio is choosen as suggestion.


Usage
---
	from spellbee.spellbee import spellbee

	if __name__ == '__main__':
		string = 'Autimattic leaarning procejures can made uss of stastical algorithmas'
		suggestions = spellbee._correct(string)
		for x in suggestions:
			print x


References:
---
<a href="http://norvig.com/spell-correct.html">Peter Norvig blog</a>

<a href="http://en.wikipedia.org/wiki/Levenshtein_distance">Levenshtein Distance</a>

<a href="http://www.ganjisaffar.com/papers/2011-Speller.pdf">qSpell</a>

<a href="http://times.cs.uiuc.edu/czhai/pub/speller-2011.pdf">CloudSpeller</a>

<a href="http://research.microsoft.com/pubs/148103/www11-onlinespellingcorrection.pdf">Query Combination Technique</a>