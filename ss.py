mine = open("mine.txt").read().split("\n")
their = open("their.txt").read().split("\n")
for line in mine:
	if line not in their:
		print line