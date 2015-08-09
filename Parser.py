from abc import ABCMeta, abstractmethod
import shutil
from codeLine import CodeLine
import cPickle as pickle

class Parser:
    __metaclass__ = ABCMeta
    
    def __init__(self, name):
        self.file_name = name
        self.create_backup()
        self.get_lines()

    @abstractmethod
    def parse(self, options):
        self.add_required()
        if options["functions"]:
            self.comb_functions()
        if options["scope"]:
            self.comb_scope()
        self.save_data()
        """ Parse the file for the given options """

    @abstractmethod
    def print_statement_open(self):
        """ Gets the print statement for this language """
    
    @abstractmethod
    def print_statement_close(self):
        """ Gets the print statement for this language """
    
    @abstractmethod
    def cPrint(self, spaces, lineNumber, newLineNumber, functionName):
        line = spaces + self.print_statement_open() + "Reached " + functionName + " at line " + str(newLineNumber) + self.print_statement_close()
        self.added_lines.append(CodeLine(line, lineNumber))

        """ Constructs the print statement and returns a CodeLine """

    @abstractmethod
    def comb_functions(self):
        """ Will go through code and comb for functions """
        
    @abstractmethod
    def comb_scope(self):
        """ Will go through code and comb for scope """
    
    @abstractmethod
    def create_backup(self):
        shutil.copy2(self.file_name, self.file_name + ".uncombed")
        """ Create backup only when the combing is successful """

    @abstractmethod
    def required(self):
        """ Gets all required imports/headers for this code """
    
    @abstractmethod
    def add_required(self):
        """ Adds all required imports/headers """
    
    @abstractmethod
    def get_lines(self):
        f = open(self.file_name, 'r')
        lines = []
        it = 1
        for line in f:
            lines.append(CodeLine(line, it))
            it = it + 1
        self.lines = lines
        self.set_meaningful_lines()
        """ Opens the file, reads all of the lines and stores them in an array of CodeLine objects """ 

    @abstractmethod
    def set_meaningful_lines(self):
        """ Parses the CodeLine array and removes any comments """

    @abstractmethod
    def save_data(self):
        with open("." + self.file_name + ".pkl", 'wb') as output:
            pickle.dump(self.added_lines, output, -1)   # Save w/ pickle so we can uncomb later
        it1 = 0
        it2 = 0
        new_lines = []
        finish_reg = False
        finish_added = False
        for i in range(len(self.lines) + len(self.added_lines) - 1):
            this_line = self.lines[it1]
            this_added_line = self.added_lines[it2]
            if not finish_reg and this_added_line.getLineNumber() <= this_line.getLineNumber():
                new_lines.append(CodeLine(this_added_line.getLine(), i))
                it2 += 1
                if it2 >= len(self.added_lines): # No more added lines...
                    finish_reg = True
                    it2 = 0
            elif not finish_added and this_added_line.getLineNumber() > this_line.getLineNumber():
                new_lines.append(CodeLine(this_line.getLine(), i))
                it1 += 1
                if it1 >= len(self.lines):  # No more regular lines...
                    finish_added = True
                    it1 = 0
            if finish_reg:
                new_lines.append(CodeLine(this_line.getLine(), i))
                it1 += 1
            elif finish_added:
                new_lines.append(CodeLine(this_added_line.getLine(), i))
                it2 += 1

        f = open(self.file_name, 'w')
        for line in new_lines:
            print str(line.getLineNumber()) + ": " + line.getLine()
            f.write(line.getLine())
