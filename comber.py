import inputHandler
from cppParser import CppParser
from cParser import CParser

class Comber:
    def __init__(self):
        self.options = inputHandler.getOptions("comb")
        
    def run(self):
        options = self.options
        self.files = options["filenames"]
        self.set_parsers()
        self.parse()

    def set_parsers(self):
        parsers = []
        for filename in self.files:
            if filename.endswith(".cpp"):
                parsers.append(CppParser(filename))
            elif filename.endswith(".c"):
                parsers.append(CParser(filename))
        self.parsers = parsers

    def parse(self):
        for parser in self.parsers:
            parser.parse(self.options)
    
if __name__ == "__main__":
    eng = Engine()
    eng.run()
