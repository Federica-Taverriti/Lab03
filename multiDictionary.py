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

    #RICERCA LINEARE
    def searchWordLinear(self, words, language):
        result = []
        dictionary = self.dictionaries[language].dict

        for w in words:
            rich = rw.RichWord(w)
            found = False
            for dword in dictionary:
                if dword == w:
                    found = True
                    break

            rich.corretta = found
            result.append(rich)
        return result

    #RICERCA DICOTOMICA (da metà)
    def searchWordDichotomic(self, words, language):
        result = []
        dictionary = self.dictionaries[language].dict

        for w in words:
            rich = rw.RichWord(w)

            left = 0
            right = len(dictionary)-1
            found = False

            while left <= right:
                mid = (left+right)//2

                if dictionary[mid] == w:
                    found = True
                    break
                elif dictionary[mid] < w:
                    left = mid + 1
                else:
                    right = mid - 1

            rich.corretta = found
            result.append(rich)

        return result