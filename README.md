# codeComber
Unix command line tool that inserts print debug lines to existing code. Written in Python.

How to use:

If on a unix machine, run ./setup.sh first.

Then,

Usage: comb [filename(s)][options]

Options:

  -h, --help       show this help message and exit

  -f, --functions  adds debug prints for each function call

  -s, --scope      adds debug prints for every new scope


Right now, only C++ and C combers are supported.


This works only for very specific coding style (for me)


It will expect the start of every new scope to be on a new line. Therefore:


int main() {

}

...would be invalid syntax. Instead, it expects this:

int main()

{

}


Likewise, it will expect if statements to be formatted like this:

if (a == b)

{

    //etc

}

