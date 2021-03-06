from Parser import Parser
from codeLine import CodeLine

class CppParser(Parser):
    def __init__(self, name):
        super(CppParser, self).__init__(name)

    def parse(self, options):
        super(CppParser, self).parse(options)

    def print_statement_open(self):
        return "std::cout << \""

    def print_statement_close(self):
        return "\" << std::endl;\n"

    def required(self):
        return "#include <iostream>\n"

    def add_required(self):
        print "Adding the required imports/headers for " + self.file_name
        # Scan imports/includes/etc. at the top of the screen
        # For C++ files we are going to assume that all #includes are together
        added_lines = []
        import_found = False
        for code_line in self.meaningful_lines:
            line = code_line.getLine()
            number = code_line.getLineNumber()
            print str(number) + ": " + line
            if line.startswith('#include'):
                if self.required() in line:
                    import_found = True
                    print "Import found!"
                    break
            else:
                break

        if not import_found:
            added_lines.append(CodeLine(self.required(), 1)) # We're inserting this at the top
        self.added_lines = added_lines

    def comb_functions(self):
        print "Combing functions for " + self.file_name
        # Look for ) then { for C++
        # Assuming that we never write code that DOESN'T follow: type name(params...) {
        # ... then this should work
        # If we ever write code that doesn't follow this format, this code will need to be changed

        for index in range(len(self.meaningful_lines)):
            code_line = self.meaningful_lines[index]
            line = code_line.getLine()
            line_number = code_line.getLineNumber()
            if "{" in line:
                # Possible start of a function. Now check if the previous one ended with a )
                previous_code_line = self.meaningful_lines[index - 1]
                previous_line = previous_code_line.getLine()
                previous_line_num = previous_code_line.getLineNumber()
                stripped_line = previous_line.strip()
                is_function = stripped_line.endswith(")") and not stripped_line.startswith("if") and not stripped_line.startswith("else")
                if is_function: 
                    # Function found
                    function_name = previous_line.split()[1].split("(", 1)[0]
                    spaces = ' ' * (len(line) - len(line.strip())) + '   '
                    new_line_number = 1 + line_number + len(self.added_lines)
                    self.cPrint(spaces, line_number + 1, new_line_number, function_name)

    def comb_scope(self):
        print "Combing scope for " + self.file_name
        num_braces = 0
        fun_found = False
        function_name = ""
        for index in range(len(self.meaningful_lines)):
            code_line = self.meaningful_lines[index]
            line = code_line.getLine()
            line_number = code_line.getLineNumber()
            if "{" in line:
                # Possible start of a function. Now check if the previous one ended with a )
                if not fun_found:
                    previous_code_line = self.meaningful_lines[index - 1]
                    previous_line = previous_code_line.getLine()
                    previous_line_num = previous_code_line.getLineNumber()

                    stripped_line = previous_line.strip()
                    is_function = stripped_line.endswith(")") and not stripped_line.startswith("if") and not stripped_line.startswith("else")
                    if is_function: 
                        # Function found
                        function_name = previous_line.split()[1].split("(", 1)[0]
                        spaces = ' ' * (len(line) - len(line.strip())) + '   '
                        new_line_number = 1 + line_number + len(self.added_lines)
                        self.cPrint(spaces, line_number + 1, new_line_number, function_name)
                        fun_found = True
                else:
                    spaces = ' ' * (len(line) - len(line.strip())) + '   '
                    new_line_number = 1 + line_number + len(self.added_lines)
                    self.cPrint(spaces, line_number + 1, new_line_number, function_name)
                num_braces += 1
            if "}" in line:
                num_braces -= 1
                if num_braces == 0:
                    fun_found = False

    def cPrint(self, spaces, lineNumber, newLineNumber, functionName):  # Construct print statement
        super(CppParser, self).cPrint(spaces, lineNumber, newLineNumber, functionName)

    def create_backup(self): 
        super(CppParser, self).create_backup()

    def get_lines(self):
        super(CppParser, self).get_lines()

    def set_meaningful_lines(self):
        beginning_of_comments = ["//" , "/*", "*"]
        meaningful_lines = []
        for line in self.lines:
            append = True
            for comment in beginning_of_comments:
                this_line = line.getLine().strip()
                if this_line.startswith(comment) or this_line.isspace() or not this_line:
                    append = False
            if append:
                meaningful_lines.append(line)
        self.meaningful_lines = meaningful_lines

    def save_data(self):
        super(CppParser, self).save_data()
