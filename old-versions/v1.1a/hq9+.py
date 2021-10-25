#!/usr/bin/env python3

########################################################
# PyHQ9+ by David Costell, 9/30/2021                   #
# Python implementation of the esoteric language HQ9+  #
# No dependencies, minimal imported modules            #
# Original HQ9+ concept by Cliff L. Biffle, 2001       #
#                                                      #
# Learn more about HQ9+ here:                          #
# http://cliffle.com/esoterica/hq9plus/                #
# Python 3.x required                                  #
########################################################
#                    PYTHON IMPORTS                    #
#                                                      #
#                                                      #
import re # will be disused soon                       #
from time import sleep # used by beer function         #
from configparser import ConfigParser # for ini        #
import os.path # for ini                               #
import sys # for version()                             #
#                                                      #
########################################################

# .INI handler 
config = ConfigParser()
existfile = os.path.isfile('cfg.ini')
if existfile == True:
    config.read('cfg.ini')
    case_sensitivity = config.get('pyhq9', 'case-sensitivity')

    if case_sensitivity == "FALSE":
        case = False
    elif case_sensitivity == "TRUE":
        case = True
    else:
        print("Error while parsing the .ini - defaulting to case-sensitivity TRUE")
        case = True
else:
    print("No ini file found, defaulting to case-sensitivity TRUE")
    case = True
# .INI handler ends here

# Initialize the shell.    
print("PyHQ9+ - HQ9+ Implementation for Python 3.x")
print("Case sensitivity: " + str(case))
print("To exit, type exit()")
print("")
accumulator = 0 # Initialize the accumulator.

# Shell
while True:
    A = input()

    if case == False: # Command Handler for non-case sensitive input
        # Hello World lowercase
        if A == "h":
            print("Hello, World!")
            print("")
        # Quine function lowercase
        re.search('[q]', A) # Search for 'q' in the input
        if re.search(r'[q]', A): # if a 'q' was found, then
            B = len(A) # Define B as the length of the input
            C = A*B # Define C as input multiplied by length of input (A * B)
            print(C) # Print the final output
            print("")

    # Normal command handler for case sensitive (default) input

    # Hello World
    if A == "H":
        print("Hello, World!")
        print("")

    # Quine function
    re.search('[Q]', A) # Search for 'Q' in the input
    if re.search(r'[Q]', A): # if a 'Q' was found, then
        B = len(A) # Define B as the length of the input
        C = A*B # Define C as input multiplied by length of input (A * B)
        print(C) # Print the final output
        print("")

    # 99 Bottles of Beer function
    if A == "9":

        def beersong():
            for i in range (99,-1,-1):            
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
                    
        beersong()

        
    # Increment the accumulator
    if A == "+":
        accumulator = accumulator + 1 # Increments the accumulator.
        print("The accumulator has been incremented.") # Notify the end user.
        print("")

    if A == "exit()":
        exit() # Exits
    if A == "version()":
        print(sys.version) # Displays Python version

    else: # if the input wasn't ANY of the above commands:

        lc = ['H', 'h', 'Q', 'q', '9', '+']
        uc = ['H', 'Q', '9', '+'] # to be used soon

        '''if case == False:
            re.search('[H, h, Q, q, 9, +]', A)
            if not re.search('[H, h, Q, q, 9, +]', A):
                print("Invalid command.")
                print("")
        elif case == True:
            re.search('[H, Q, 9, +]', A)
            if not re.search(r'[H, Q, 9, +]', A):
                print("Invalid command.")
                print("")'''
    
# Shell ends here

                  
# Version 1.1a
