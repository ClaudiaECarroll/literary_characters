import re
text = open("filenameTh.txt", "r")
text = str(text.read())
chapters = re.split("Chapter ", text, flags = re.IGNORECASE)
chapters.pop(0)
for i in range(1, len(chapters)+1):
	writetext = open("{}.txt".format(i), "w+")
	writetext.write(chapters[i-1])
	writetext.close()
