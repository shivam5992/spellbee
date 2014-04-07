data = open("out1.txt").read().split("\n")
f = open("out.txt","w")
for line in data:
	line = line.strip()
	if line:
		line1 = line.replace("-"," ")
		line1 = line1.replace("_"," ")	
		f.write(line1 + "\n")