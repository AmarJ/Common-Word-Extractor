#mikeli sucks
import re

listOfTexts = {"test test testing tester tester test test", "test test testing tester tester test test", "test test testing tester tester test test. The car"}

commonWords = {}

def extract(texts):
    for text in texts:
        wordList = re.sub("[^\w]", " ",  text).split()

        for word in wordList:
            if (word in commonWords):
                commonWords[word]+=1 
            else:
                commonWords[word] = 1

    return commonWords


wordsUsed = extract(listOfTexts)

sortedList = [(k, wordsUsed[k]) for k in sorted(wordsUsed, key=wordsUsed.get, reverse=True)]
for k,v in sortedList:
    print("'"+k+"' is used "+str(v)+" times.")
