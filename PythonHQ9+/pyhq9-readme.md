# PythonHQ9+ by David Costell (DontEatThemCookies)

Original concept by Cliff L. Biffle, 2001

This readme file contains some basic information on how PythonHQ9+ works. 
It also gives you information on the premise of HQ9+ itself.

# Table of Contents

<!--ts-->
   * [HQ9+](#hq9)
   * [PythonHQ9+](#pythonhq9)
     * [Shell](#shell-implementation-hq9py)
     * [Interpreter](#interpreter-implementation-interpreter-hq9py)
     * [Compiler](#compiler-implementation-compiler-hq9py)
   * [Dependencies](#dependencies)
   * [License](#license)
   * [How to Install](#how-to-install)
<!--te-->

## HQ9+

The original HQ9+ specification popped up in 2001. It was not Turing-complete, and it had a mere 4 instructions. It was also classified as a joke language. Over time, HQ9+ got recognized in the esoteric language community, with many implementations popping up, with interpreters written in C, Pascal, JavaScript, PHP and others, as well as new variants. This included HQ9++, HQ9+-, HQ9+~, HQ9F+, CHIQRSX9+, HQ9+B, and many more. All of these variants had something new to offer, one variant even makes it Turing-complete. You can find resources on HQ9+ and its variants below:

[Esolang Wiki](https://esolangs.org/wiki/HQ9%2B) - 
[Biffle's Blog](http://cliffle.com/esoterica/hq9plus/)



## PythonHQ9+

After 20 years from the original implementation of HQ9+, I discovered it. Simply perplexed yet impressed, I decided that this
joke language was very effective at being just that: a joke language. Previously I had only made one attempt to make an esolang,
but that project was scrapped almost immediately. I decided to write an implementation of this, and I did so in Python 3.

PythonHQ9+ is theoretically compliant with HQ9+'s original specification. Two versions of the implementation exist: the shell and
the interpreter. Both are very similar, but they will be differentiated below:

***
### Shell implementation (hq9+.py)

This script simulates a shell instance. In this shell, you can input the following commands:

H - prints "Hello, World!"

Q - prints a multiplied version of itself (also called a quine)
For example, if you input "Q", the shell will return "QQ", and if you input "QQ", it will return QQQQ.

9 - prints the lyrics to "99 Bottles of Beer."

\+ - Increments the accumulator. 
The accumulator initializes at the value "0", but it is not directly accessible.

From version 1.0a onwards, you can create an optional file called "cfg.ini" and place it on the same
directory the script is on. The format is:
```ini
[pyhq9]
case-sensitivity = [TRUE/FALSE]
```
If it is set to TRUE, only uppercase/capitalized letters will be accepted as input.
If it is set to FALSE, both uppercase and lowercase letters will be accepted.

If you do not create the config file, it will still work with no hindrance on the functionality, but case
sensitivity will always be set to TRUE (uppercase only). 
***
### Interpreter implementation (interpreter-hq9+.py)

This script takes input from a file. It can be any format, but you can use txt.
You must specify either the path to the input file, or the name of the file.
However, you must place the input file in the same folder as the .py file if you choose to do the latter.
Invalid paths/filenames will result in a Python error.

Once a valid path/filename is entered, the interpreter begins its work.
It checks for the following characters: (It is case-sensitive, only detecting capitalized letters)

H - prints "Hello, World!"

Q - prints a multiplied version of itself (also called a quine)
For example, if you input "Q", the shell will return "QQ", and if you input "QQ", it will return QQQQ.

9 - prints the lyrics to "99 Bottles of Beer."

\+ - Increments the accumulator. 
The accumulator initializes at the value "0", but it is not directly accessible.

Operations are executed based on the order of the original initialism: H, Q, 9, +
For example, a file with the following input: 
```
HQ+H
```
would be interpreted as:
```
Hello, World! Hello, World!
QQ
Accumulator incremented by 1!
```

***
### Compiler implementation (compiler-hq9+.py)

This script takes user input (must be valid HQ9+) from the console and "compiles" (translates) the code to Python 3.
First it will prompt you what to name the file, and then the actual commands to specify.
This implementation is still a Beta, and as such no guarantees on completeness are made on this compiler.

The commands are as follows:

H - prints "Hello, World!"

Q - prints a multiplied version of itself (also called a quine)
For example, if you input "Q", the shell will return "QQ", and if you input "QQ", it will return QQQQ.

9 - prints the lyrics to "99 Bottles of Beer."

\+ - Increments the accumulator. 
The accumulator initializes at the value "0", but it is not directly accessible.

The compiler translates the input based on the order of the original initialism: H, Q, 9, +
For example, if the input was:
```
HHQQH
```
then the compiler's full output file would be (as of Beta 3):
```py
#!/usr/bin/env python3 
#Compiled by the PyHQ9+ Compiler (Python 3) - 2021-10-01 13:01:58.386800 
A = 'HHQQH' 
acm = 0 # Accumulator 
 
H = A.count('H') # Hello World 
print(H*'Hello, World! ') 
 
q1 = A.count('Q') # Quine function 
q2 = q1 * q1 
print(q2*'Q') 
 
 
 
 
 
input('Press any key to continue...')
```

Should a filename specified by the user conflict with an existing file that uses the same name, the compiler will throw an error and give you an option to delete the file. Normally this is not recommended, as you can simply re-launch the compiler and specify a different filename.

From Release Candidate 1 onwards, you can create an optional file called "cfg.ini" and place it on the same
directory the script is on. If you already have a "cfg.ini" file for the shell, you may simply append it to the end of the file. The format is:
```ini
[compiler]
inputype = USER
```

USER - Compiler will take input from user (Default)
FILE - Compiler will take input from a file 

## Dependencies
PythonHQ9+ aims to be as dependency-free as possible. As of Version 1, there are no external modules needed for PythonHQ9+
(you don't have to run pip install whateverpackage) and it is extremely likely future versions will also not need them.

## License
PythonHQ9+ is licensed under the permissive MIT License. The original .py files are of my authorship, and the HQ9+ concept
is credited to Cliff L. Biffle.

## How to Install
You can download the binaries in the latest release and extract them to a folder.
Alternatively, you can either clone the repository or download a ZIP, then navigate to the PythonHQ9+ folder and run the scripts.

If you haven't figured out by now, you will need Python itself for the scripts to work. If you wish, you can [download the latest Python version](https://www.python.org/downloads/) for optimal results, but PyHQ9+ has been tested in 3.6 and it still works as intended. I do not recommend 3.5 or older.


***
PythonHQ9+ Readme.md - Version 5, October 11, 2021  
