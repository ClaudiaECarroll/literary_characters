import re
import sys

filename = sys.argv[1]
name = filename.split(".")

text = open(filename, "r")
text = str(text.read())
chapters = re.split("Chapter ", text, flags = re.IGNORECASE)
chapters.pop(0)
for i in range(1, len(chapters)+1):
	writetext = open(str(name[0]) + "_" + str(i).zfill(4) + ".txt", "w+")
	writetext.write(chapters[i-1])
	writetext.close()
