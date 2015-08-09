import inputHandler
from codeLine import CodeLine
import cPickle as pickle
import os

class Uncomber:
    def __init__(self):
        self.options = inputHandler.getOptions("uncomb")

    def run(self):
        file_names = self.options["filenames"]
        for f in file_names:
            self.uncomb(f)

    def uncomb(self, f):
        fi = open(f, 'r')
        with open('.' + f + '.pkl', 'r') as input:
            appended_lines = pickle.load(input)
        new_lines = []
        rLines = []
        for line in appended_lines:
            print line.getLine()
            rLines.append(line.getLine())
        for line in fi:
            if not line in rLines:
                new_lines.append(line) 
        fi = open(f, 'w')
        for line in new_lines:
            print line
            fi.write(line)
        os.remove(f + '.uncombed')
        os.remove('.' + f + '.pkl')
