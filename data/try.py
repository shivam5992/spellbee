#data = open('mydic.txt').read().split("\n")
#import json

out = open('dic.txt').read().split("\n")

for ind, line in enumerate(out):
	line = line.replace("'","")
	print "'" + line + "':'" + line + "',"

	
# out = json.dumps(res)
# fout = open('mydic.py', 'w')
# fout.write(out)		