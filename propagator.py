class propagator:
    def __init__(self, element):
        self.vertexfrom = element.find("from").text
        self.vertexto = element.find("to").text
        self.field = element.find("field").text
    def texprint(self, file, particledict):
        file.write("{} -- [ {}, edge label=\({}\) ] {},\n ".format(self.vertexfrom, particledict[self.field], self.field ,self.vertexto))
