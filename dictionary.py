class Dictionary:
    def __init__(self):
        self._dict = []

    def loadDictionary(self,path):
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                word = line.strip().lower()
                self._dict.append(word)

    def printAll(self):
        for w in self._dict:
            print(w)


    @property
    def dict(self):
        return self._dict