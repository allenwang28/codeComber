from Parser import Parser

class CppParser(Parser):
    def __init__(self, name):
        super(CppParser, self).__init__(name)

    def parse(self, options):
        super(CppParser, self).parse(options)

    def print_statement_open(self):
        return "std::cout << "

    def print_statement_close(self):
        return "<< std::endl;"

    def required(self):
        return "#include <iostream>"

    def comb_functions(self):
        print "Combing functions for " + self.file_name

    def comb_scope(self):
        print "Combing scope for " + self.file_name

    def create_backup(self): 
        super(CppParser, self).create_backup()

    def update_file(self):
        print "Update files for " + self.file_name
