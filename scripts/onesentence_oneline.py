import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
file = open("filename.txt")
content = file.read()
sentences = nltk.sent_tokenize(content)
newfile = open("filename.txt", "w")
for token in sentences:
    newfile.write(token)
    newfile.write("\n")
