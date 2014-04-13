from pprint import pprint
import re

data = open("data/sentiwordnet.txt", "r").read()
lines = data.split("\n")
out = open("out.txt","w")
result = []
for x,line in enumerate(lines):
	print x
	
	line = line.split("	")
	word = line[4]
	mWords = word.split(" ")
	if len(mWords) != 1:	
		for word in mWords:
			index = word.find('#')
			if index > -1:
				word = word[:index]
			out.write(word + "\n")
	else:
		index = word.find('#')
		if index > -1:
			word = word[:index]
		out.write(word + "\n")