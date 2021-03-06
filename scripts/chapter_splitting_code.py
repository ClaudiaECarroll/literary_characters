import re
import sys

filename = sys.argv[1]
name = filename.split(".")

text = open(filename, "r")
text = str(text.read())
if "Chapter" in text:
    chapters = re.split("Chapter ", text)
    chapters.pop(0)
    for i in range(1, len(chapters)+1):
        writetext = open(str(name[0]) + "_" + str(i).zfill(4) + ".txt", "w+")
        writetext.write(chapters[i-1])
        writetext.close()
elif "CHAPTER" in text:
    chapters = re.split("CHAPTER ", text)
    chapters.pop(0)
    for i in range(1, len(chapters)+1):
        writetext = open(str(name[0]) + "_" + str(i).zfill(4) + ".txt", "w+")
        writetext.write(chapters[i-1])
        writetext.close()
#elif re.match("^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"):
    #pattern_split = re.compile(r"^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")
    #chapters = pattern_split.split(text)
    #chapters.pop(0)
    #for i in range(1, len(chapters)+1):
        #writetext = open(str(name[0]) + "_" + str(i).zfill(4) + ".txt", "w+")
        #writetext.write(chapters[i-1])
        #writetext.close()
