from optparse import OptionParser

list_of_options = [
        "filenames", 
        "functions", 
        "scope"]

supported_file_types = [
        ".cpp",
        ".c",
        ".py"]

def readOptions():
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
        filenames.append(arg)

    return [options, filenames]


def not_supported(arg):
    for ending in supported_file_types:
        if arg.endswith(ending):
            return False
    return True


def getOptions():
    opts = readOptions()
    options = {}
    options["filenames"] = opts[1]
    options["functions"] = opts[0].functions
    options["scope"] = opts[0].scope
    return options
