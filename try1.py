from lemmatize import *
data = open("test1.txt").read().split("\n")

for word in data:
	word1 = step1a(word)
	word1 = step1b(word1)
	word1 = postStep1b(word1)
	word1 = step1c(word1)
	word1 = step2(word1)
	word1 = step3(word1)
	word1 = step4(word1)
	word1 = step5a(word1)
	word1 = step5b(word1)
	print word, word1