import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
       self.dictionaries = {}

       it = d.Dictionary()
       it.loadDictionary("resources/Italian.txt")

       en = d.Dictionary()
       en.loadDictionary("resources/English.txt")

       es = d.Dictionary()
       es.loadDictionary("resources/Spanish.txt")

       self.dictionaries["italian"] = it
       self.dictionaries["english"] = en
       self.dictionaries["spanish"] = es

    def printDic(self, language):
        self.dictionaries[language].printAll()

    def searchWord(self, words, language):
        result = []
        dictionary = self.dictionaries[language].dict

        for w in words:
            rich = rw.RichWord(w)
            if w in dictionary:
                rich.corretta = True
            else:
                rich.corretta = False

            result.append(rich)

        return result