class Files:
    def __init__(self,name):
        self.file = open(name).read()

    def readSentences(self):
        return self.file.split("\n")

    
