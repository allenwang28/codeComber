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
        # Scan imports/includes/etc. at the top of the screen
        # For C++ files we are going to assume that all #includes are together
        for line in self.lines:
            print line.getLine()
        
         
        # If the import is not included, add it

        # Then 

    def comb_scope(self):
        print "Combing scope for " + self.file_name

    def create_backup(self): 
        super(CppParser, self).create_backup()

    def update_file(self):
        print "Update files for " + self.file_name

    def get_lines(self):
        super(CppParser, self).get_lines()

    def remove_comments(self):
        beginning_of_comments = ["//" , "/*", "*"]
        meaningful_lines = []
        for line in self.lines:
            for comment in beginning_of_comments:
                if not line.getLine().startswith(comment):
                    meaningful_lines.append(line)
        self.lines = meaningful_lines
