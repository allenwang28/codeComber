from Parser import Parser

class CParser(Parser):
    def __init__(self, name):
        super(CParser, self).__init__(name)

    def parse(self, options):
        super(CParser, self).parse(options)

    def print_statement_open(self):
        return "printf(\""

    def print_statement_close(self):
        return "\"\\n);"

    def required(self):
        return "#include <stdio>"

    def comb_functions(self):
        print "Combing functions for " + self.file_name
        
        # Scan imports/includes/etc. at the top of the screen
         
        # If the import is not included, add it

        # Then 

    def comb_scope(self):
        print "Combing scope for " + self.file_name

    def create_backup(self): 
        super(CParser, self).create_backup()

    def update_file(self):
        print "Update files for " + self.file_name
