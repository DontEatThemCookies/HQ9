#!/usr/bin/env python3
"""
Phoenix HQ9+ Engine - BETA 2
Python 3

The following software is in the Beta stage.
Bugs may occur, tread with caution.

Part of the PythonHQ9+ project by David Costell
https://github.com/DontEatThemCookies/HQ9

HQ9+ is an esoteric language by Cliff Biffle.
Learn more about it through the below links:
http://cliffle.com/esoterica/hq9plus/
https://esolangs.org/wiki/HQ9%2B

12/4/2021
"""

def main():
    # IMPORTS
    import sys

    # FUNCTIONS
    def _help_():
        """
        This function displays usage help when
        the engine is launched with the -h argument.
        """
        print("Help on Phoenix Engine:")
        print()
        print("python phoenix.py [input filename] {output filename} {-h}")
        print("[input filename] - Specify name of the file to interpret/transcompile.")
        print("[output filename] - Specify name of the output file (must be specified for transcompilation)")
        print("[-h] - Optional flag. Displays this help prompt.")

    def repl():
        """
        Phoenix Engine REPL (Read-Evaluate-Print-Loop)

        Similar to Python's own REPL.
        Takes user input, evaluates for instructions,
        executes them and stands by for more input.
        """
        accumulator = 0
        print("Phoenix HQ9+ Engine - BETA")
        print("PythonHQ9+ v2.0 by David Costell")
        print("REPL Mode - type help() for help")
        print("")
        while True:
            # Input loop
            instruction = input(">>> ")

            if instruction == "help()":
                print("REPL Help:")
                print("")
                print("help() - Displays this help message.")
                print("version() - Displays the Engine's version.")
                print("exit() - Exits the Engine.")

            # Instruction Parser
            if "H" or "h" in instruction:
                # Hello, World!
                for _ in range(instruction.upper().count("H")):
                    print("Hello, World!")

            if "Q" or "q" in instruction:
                # Quine
                for _ in range(instruction.upper().count("Q")):
                    print("Q" * instruction.upper().count("Q"))

            if "9" in instruction:
                # 99 Bottles of Beer
                for _ in range(instruction.upper().count("9")):
                    beer = 99
                    while beer > 0:
                        print(beer, "bottles of beer on the wall,", beer, "bottles of beer")
                        beer = beer-1
                        print("Take one down, pass it around,", beer, "bottles of beer on the wall")
                        print("")
                        if beer == 2:
                            print(beer, "bottles of beer on the wall,", beer, "bottles of beer")
                            beer = beer - 1
                            print("Take one down, pass it around,", beer, "bottle of beer on the wall")
                            print("")
                        if beer == 1:
                            print(beer, "bottle of beer on the wall,", beer, "bottle of beer")
                            beer = beer - 1
                            print("Take one down, pass it around,", beer, "bottles of beer on the wall")
                            print("")
                        if beer == 0:
                            break
                    print("No more bottles of beer on the wall, no more bottles of beer.")
                    print("Go to the store and buy some more, 99 bottles of beer on the wall.")

            if "+" in instruction:
                for _ in range(instruction.count("+")):
                    accumulator = accumulator + 1

            if instruction == "version()":
                print("Phoenix HQ9+ Engine")
                print("Version BETA 2")
            if instruction == "exit()":
                exit()

    def interpreter(file):
        """
        Phoenix Engine Interpreter

        Interprets and execute an HQ9+ source file.
        """
        accumulator = 0
        try:
            sourcefile = open(file)
        except FileNotFoundError:
            print("Error: the specified file was not found.")
            print()
            print("Ensure the filename was correctly spellled")
            print("and that the specified file exists.")
            input();exit()
        linelist = []
        for line in sourcefile:
            linelist.append(line.strip())
        line = "".join(linelist)

        # Instruction Parser
        if "H" or "h" in line:
            # Hello, World!
            for _ in range(line.upper().count("H")):
                print("Hello, World!")

        if "Q" or "q" in line:
            # Quine
            for _ in range(line.upper().count("Q")):
                print("Q" * line.upper().count("Q"))

        if "9" in line:
            # 99 Bottles of Beer
            for _ in range(line.upper().count("9")):
                beer = 99
                while beer > 0:
                    print(beer, "bottles of beer on the wall,", beer, "bottles of beer")
                    beer = beer-1
                    print("Take one down, pass it around,", beer, "bottles of beer on the wall")
                    print("")
                    if beer == 2:
                        print(beer, "bottles of beer on the wall,", beer, "bottles of beer")
                        beer = beer - 1
                        print("Take one down, pass it around,", beer, "bottle of beer on the wall")
                        print("")
                    if beer == 1:
                        print(beer, "bottle of beer on the wall,", beer, "bottle of beer")
                        beer = beer - 1
                        print("Take one down, pass it around,", beer, "bottles of beer on the wall")
                        print("")
                    if beer == 0:
                        break
                print("No more bottles of beer on the wall, no more bottles of beer.")
                print("Go to the store and buy some more, 99 bottles of beer on the wall.")

        if "+" in line:
            for _ in range(line.count("+")):
                accumulator = accumulator + 1

        print("-" * 40)
        print("Execution complete.")
        input("Press ENTER to exit.")

    def transcompiler(file, output):
        """
        Phoenix Engine Transcompiler (Source-to-Source Compiler)

        Compiles HQ9+ source file to Python 3.
        """
        try:
            sourcefile = open(file)
        except FileNotFoundError:
            print("Error: the specified file was not found.")
            print()
            print("Ensure the filename was correctly spellled")
            print("and that the specified file exists.")
            input();exit()
        outputfile = open(output, "w")
        instructionlist = []
        linelist = []
        for line in sourcefile:
            linelist.append(line.strip())

        # Instruction Parser
        # Hello, World!
        instructionlist.append("""
for _ in range(line.upper().count("H")):
    print("Hello, World!")""")

        # Quine
        instructionlist.append("""
for _ in range(line.upper().count("Q")):
    print("Q" * line.upper().count("Q"))""")

        # 99 Bottles of Beer
        instructionlist.append("""
for _ in range(line.upper().count("9")):
    beer = 99
    while beer > 0:
        print(beer, "bottles of beer on the wall,", beer, "bottles of beer")
        beer = beer-1
        print("Take one down, pass it around,", beer, "bottles of beer on the wall")
        print("")
        if beer == 2:
            print(beer, "bottles of beer on the wall,", beer, "bottles of beer")
            beer = beer - 1
            print("Take one down, pass it around,", beer, "bottle of beer on the wall")
            print("")
        if beer == 1:
            print(beer, "bottle of beer on the wall,", beer, "bottle of beer")
            beer = beer - 1
            print("Take one down, pass it around,", beer, "bottles of beer on the wall")
            print("")
        if beer == 0:
            break
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.")""")

        # Accumulator
        instructionlist.append("""
for _ in range(line.count("+")):
    accumulator = accumulator + 1""")

        finalline = "".join(linelist)
        outputfile.write("#!/usr/bin/env python3"+"\n")
        outputfile.write("\n")
        outputfile.write("# Transcompiled to Python 3 by the Phoenix Engine"+"\n")
        outputfile.write("\n"+"line = '{}'".format(finalline)+"\n")
        outputfile.write("accumulator = 0"+"\n")
        for i in instructionlist:
            outputfile.write(i+"\n")
        outputfile.write("\n"+"input()"+"\n")
        print("Transcompilation succeeded (outputfile.py)")
        input("Press ENTER to exit.")

    # ARGUMENT PARSING
    try:
        # Check for first argument
        param1 = sys.argv[1]
        if param1 == "-h":
            # Help
            _help_()
        else:
            filename = param1
            try:
                # Transcompiler
                transcompiler(filename, sys.argv[2])
            except IndexError:
                # Interpreter
                interpreter(filename)
    except IndexError:
        # REPL Mode
        repl()

if __name__ == "__main__": main() # Entry Point