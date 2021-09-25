# PythonHQ9+ by David Costell

Original concept by Cliff L. Biffle, 2001

This readme file contains some basic information on how PythonHQ9+ works. 
It also gives you information on the premise of HQ9+ itself.

# Table of Contents

<!--ts-->
   * [HQ9+](#hq9)
   * [PythonHQ9+](#pythonhq9)
     * [Shell](#shell-implementation-hq9py)
     * [Interpreter](#interpreter-implementation-interpreter-hq9py)
   * [Dependencies](#dependencies)
   * [License](#license)
   * [How to Install](#how-to-install)
<!--te-->

## HQ9+

The original HQ9+ implementation popped up in 2001. It was not Turing-complete, and it had a mere 4 instructions.
It is also classified as a joke language. Over time, HQ9+ got recognized in the esoteric language community, with 
many other implementations popping up, with interpreters written in C, Pascal, JavaScript, PHP and others, as well
as new variants. This included HQ9++, HQ9+-, HQ9+~, HQ9F+, CHIQRSX9+, HQ9+B, and many more. All of these variants had
something new to offer, one variant even makes it Turing-complete. You can find resources on HQ9+ and its variants below:

https://esolangs.org/wiki/HQ9%2B
http://cliffle.com/esoterica/hq9plus/



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

Inputting anything else will result in a simulated error, stating "Invalid command." 
Do note that the shell is case-sensitive. It will throw the aforementioned simulated error if you enter
lowercase letters.
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

P - Increments the accumulator. 
The accumulator initializes at the value "0", but it is not directly accessible.

You will notice that the command to increment the accumulator is different from the one in the shell.
The plus sign (+) had to be substituted for P due to an error with the RegEx module. A fix to this has not yet been found.

Operations are executed based on the order of the original initialism: H, Q, 9, + (P in this case)
For example, a file with the following input: 
```
HQPH
```
would be interpreted as:
```
Hello, World! Hello, World!
QQ
Accumulator incremented by 1!
```

## Dependencies
PythonHQ9+ aims to be as dependency-free as possible. As of Version 1, there are no external modules needed for PythonHQ9+
(you don't have to run pip install whateverpackage) and it is extremely likely future versions will also not need them.

## License
PythonHQ9+ is licensed under the permissive MIT License. The original .py files are of my authorship, and the HQ9+ concept
is credited to Cliff L. Biffle.

## How to Install
You can either clone the repository or download a ZIP, then navigate to the PythonHQ9+ folder and run the scripts.
A Release will be published soon, for easier set up.

***
PythonHQ9+ Readme.md - Version 1, September 25, 2021  
