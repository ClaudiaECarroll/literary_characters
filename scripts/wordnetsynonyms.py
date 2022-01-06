from nltk.corpus import wordnet
import io

synonyms = []

file = io.open(FILENAME, mode="r", encoding="utf8")
dictionaryread = file.read()
dictionary = dictionaryread.split()

for word in dictionary:
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())

newdictionary = set(dictionary).union(set(synonyms))

print(newdictionary)
