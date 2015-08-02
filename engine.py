import inputHandler

class Engine:
    def __init__(self):
        self.options = inputHandler.getOptions()
        
    def run(self):
        options = self.options
        if options["functions"]:
            combFunctions()
        if options["scope"]:
            combScope()


if __name__ == "__main__":
    eng = Engine()
    eng.run()
