import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multiDict = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        txtIn = replaceChars(txtIn.lower())
        words = txtIn.split()

        start = time.time()
        result = self.multiDict.searchWord(words, language)
        end = time.time()

        errors = []
        for r in result:
            if not r.corretta:
                errors.append(str(r))

        print("-----------------------------")
        print("Using contains")

        for e in errors:
            print(e)

        print(f"Time elapsed: {end - start}")

        #LINEAR SEARCH
        start = time.time()
        result = self.multiDict.searchWordLinear(words, language)
        end = time.time()

        print("-----------------------------")
        print("Using Linear search")

        for r in result:
            if not r.corretta:
                print(r)

        print(f"Time elapsed: {end - start}")

        #DICHOTOMIC SEARCH
        start = time.time()
        result = self.multiDict.searchWordDichotomic(words, language)
        end = time.time()

        print("-----------------------------")
        print("Using Dichotomic search")

        for r in result:
            if not r.corretta:
                print(r)

        print(f"Time elapsed: {end - start}")

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\/*{}[]()#-_.!$%^;:,~\"'?"

    for c in chars:
        text = text.replace(c, "")

    return text