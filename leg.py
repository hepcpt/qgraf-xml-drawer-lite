class leg:
    def __init__(self, element):
        self.vertex = element.find("vertex").text
        self.momentum = element.find("momentum").text
        self.field = element.find("field").text
    def texprint(self, file, particledict):
        file.write("{} [particle=\({}\)] -- [ {} ] {},\n ".format(self.momentum, self.field ,particledict[self.field], self.vertex))
