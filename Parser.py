from abc import ABCMeta, abstractmethod
import shutil

class Parser:
    __metaclass__ = ABCMeta
    
    def __init__(self, name):
        self.file_name = name
        self.create_backup()

    @abstractmethod
    def parse(self, options):
        self.create_backup()
        if options["functions"]:
            self.comb_functions()
        if options["scope"]:
            self.comb_scope()
        """ Parse the file for the given options """

    @abstractmethod
    def print_statement_open(self):
        """ Gets the print statement for this language """
    
    @abstractmethod
    def print_statement_close(self):
        """ Gets the print statement for this language """
    
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
    def update_file(self):
        """ Will save the new file """

    @abstractmethod
    def required(self):
        """ Gets all required imports/headers for this code """
