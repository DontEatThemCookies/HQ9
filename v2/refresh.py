#!/usr/bin/env python3

########################################################
# PyHQ9+ by David Costell, 10/25/2021                  #
# Python implementation of the esoteric language HQ9+  #
# Original HQ9+ concept by Cliff L. Biffle, 2001       #
# Version 2.0 (PyHQ9+ Refresh)                         #
#                                                      #
# Learn more about HQ9+ here:                          #
# http://cliffle.com/esoterica/hq9plus/                #
# Python 3.x required                                  #
########################################################


# Attention! This version of PythonHQ9+ v2.0 is in its early
# BETA stages, and should not be treated as production-ready.
# Bugs are to be expected! If you see one, please report them
# by creating a new issue in the repo. Thank you.


# IMPORTS #
from time import sleep
from configparser import ConfigParser as cfg
import os.path
import sys

# FUNCTIONS #

def beersong(): # 99 Bottles
    for i in range (99, -1, -1):
        if i > 2:
            print(i, "bottles of beer on the wall,", i, " bottles of beer,")
            print("Take one down and pass it around,", i-1, "bottles of beer on the wall.\n")
            sleep(0.1)      
        elif i == 2:
                print(i, "bottles of beer on the wall,", i, " bottles of beer,")
                print("Take one down and pass it around,", i-1, "bottle of beer on the wall.\n")
                sleep(0.1)
        elif i == 1:
                print(i, "bottle of beer on the wall,", i, " bottle of beer,")
                print("Take one down and pass it around,", i-1, "bottles of beer on the wall.\n")
                sleep(0.1)
        else:
            print("No more bottles of beer on the wall, no more bottles of beer.")
            print("Go to the store and buy some more, 99 bottles of beer on the wall.")
            sleep(0.5)
acm = 0 # Accumulator

# Prevent being imported as a module
if __name__ != "__main__":
    exit()

# Configuration Handler
cfg = cfg()
exist = os.path.isfile('cfg.ini')
if exist == True:
    cfg.read('cfg.ini')
    lcase = cfg.get('pyhq9', 'case-sensitivity')
    if lcase.upper() == "TRUE":
        case = True
    elif lcase.upper() == "FALSE":
        case = False
    else:
        print('Case sensitivity defaulted to TRUE.')
        case = True
else:
    print('No config file, defaulted to TRUE.')
    case = True

# Main screen
print("PythonHQ9+ v2 - Refreshed HQ9+ implementation in Python")
print("Case sensitivity:", case)
print("exit() to terminate the shell.")
print("")

# Input loop
while True:
    cmd = input()

    # Case-Insensitive commands
    if case == False:
        if cmd.upper() == "H":
            print("Hello, World!")
            print("")
        if "Q" in cmd.upper():
            cmd = "".join(c for c in cmd if c.isalpha()) # Sanitization
            length = len(cmd)
            output = cmd*length
            print(output.upper())
            print("")
            
    # Case-Sensitive commands
    elif case == True:
        if cmd == "H":
            print("Hello, World!")
            print("")
        if "Q" in cmd:
            cmd = "".join(c for c in cmd if c.isalpha()) # Sanitize
            length = len(cmd)
            output = cmd*length
            print(output.upper())
            print("")
    if cmd == "9":
        beersong()
        print("")
    if cmd == "+":
        acm=acm+1
        print("Accumulator incremented.")
        print("")

    # Shell commands (commands not part of HQ9+)
    if cmd == "exit()":
        exit()
    if cmd == "version()":
        print(sys.version)
        print("")

    else: # Handles invalid input.
        cmds = ["H", "Q", "9", "+", "H", "Q", "h", "q", "9", "+"]
        if case == True:
            if any((c in cmds[0:4]) for c in cmd):
                print("")
            else:
                print("Invalid command.")
        else:
            if any((c in cmds[4:10]) for c in cmd):
                print("")
            else:
                print("Invalid command.")
                
# Version 2.0 - Beta 1
