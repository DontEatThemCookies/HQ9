HQ9+ Engine (PythonHQ9+ v2.0) - codename Phoenix

Current Version: v1

A full HQ9+ interpreter engine, featuring 
a REPL, an interpreter and a transcompiler 
to Python 3.

100% HQ9+ specification compliance, as specified in http://cliffle.com/esoterica/hq9plus/
Consolidated - REPL, Compiler and Interpreter unified in one engine
Easy and intuitive usage, simple design
Optimized to run faster than PyHQ9+ v1
Overall a huge improvement over PyHQ9+ v1

All instructions are case-insensitive in the Phoenix Engine.

-------------------------------------------------------------------------------------------------

USAGE

$ python phoenix.py [input filename] [output filename].py [-h]

All arguments are optional.
To enter REPL mode, simply launch the engine without arguments.

To directly interpret a file, do "python phoenix.py [input filename]"
Example: python phoenix.py myscript.txt

To transcompile a file, do "python phoenix.py [input filename] [output filename]"
Example: python phoenix.py myscript.txt myoutput.py
Output filename must end with ".py"

[input filename] The name of the source HQ9+ file to interpret/transcompile.
[output filename] The name of the Python 3 file to transcompile to. Only used for transcompilation.
[-h] Displays help.

-------------------------------------------------------------------------------------------------

DOCUMENTATION

PythonHQ9+ v2 documentation can be found in the official GitHub repository wiki
https://github.com/DontEatThemCookies/HQ9/wiki/PyHQ9--Documentation-v2