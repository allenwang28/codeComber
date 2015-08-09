from optparse import OptionParser
import sys
import os.path

list_of_options = [
        "filenames", 
        "functions", 
        "scope"]

supported_file_types = [
        ".cpp",
        ".c",
        ".py"]

def readOptions(t):
    usage = "usage: %prog [filename(s)] [options]"
    parser = OptionParser(prog='comb', usage=usage)

    parser.add_option('-f', '--functions', dest='functions', action='store_true', help='adds debug prints for each function call')
    parser.add_option('-s', '--scope', dest='scope', action='store_true', help='adds debug prints for every new scope')
    parser.set_defaults(scope = False)
    parser.set_defaults(functions = True)

    options, args = parser.parse_args()

    if not args:
        parser.error('No file name was given')

    if options.scope:
        options.functions = False

    filenames = []
    for arg in args:
        if not_supported(arg):
            parser.error('Unsupported file type')
        if not os.path.isfile(arg):
            parser.error("File doesn't exist")
        if os.path.isfile(arg + ".uncombed"):
            if t == "comb":
                if not verify_comb():
                    sys.exit(0)
        else:
            if t == "uncomb":
                parser.error("File has never been combed!")
        filenames.append(arg)

    return [options, filenames]

def verify_comb():
    valid = {"yes": True, "y": True, "ye": True, "no": False, "n": False}
    print("This file has already been combed.")
    default = "yes"
    while True:
        sys.stdout.write("Are you sure you want to continue? (Y/n): ")
        choice = raw_input().lower()
        if choice == "":
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no'\n")
    

def not_supported(arg):
    for ending in supported_file_types:
        if arg.endswith(ending):
            return False
    return True


def getOptions(t):
    opts = readOptions(t)
    options = {}
    options["filenames"] = opts[1]
    options["functions"] = opts[0].functions
    options["scope"] = opts[0].scope
    return options
