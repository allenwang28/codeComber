from Parser import Parser
from cppParser import CppParser

class CParser(CppParser): # C will be very similar to C++ but with different print statements
    def __init__(self, name):
        super(CParser, self).__init__(name)

    def parse(self, options):
        super(CParser, self).parse(options)

    def print_statement_open(self):
        return "printf(\""

    def print_statement_close(self):
        return "\\n\");\n"

    def required(self):
        return "#include <stdio>\n"

    def comb_functions(self):
        super(CParser, self).comb_functions()
        
    def comb_scope(self):
        super(CParser, self).comb_scope()

    def cPrint(self, spaces, lineNumber, newLineNumber, functionName):
        super(CParser, self).cPrint(spaces, lineNumber, newLineNumber, functionName)

    def create_backup(self): 
        super(CParser, self).create_backup()

    def get_lines(self):
        super(CParser, self).get_lines()

    def set_meaningful_lines(self):
        super(CParser, self).set_meaningful_lines()

    def save_data(self):
        super(CParser, self).save_data()
