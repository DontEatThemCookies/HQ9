#!/usr/bin/env python3

########################################################
# PyHQ9++ Interpreter by David Costell, 9/28/2021      #
# Python implementation of HQ9++, an HQ9+ variant.     #
# Interprets commands from a file instead of a shell.  #
# Original HQ9+ concept by Cliff L. Biffle, 2001       #
# HQ9++ specification by David Morgan Mar              #
#                                                      #
# Learn more about HQ9+ and HQ9++ here:                #
# http://cliffle.com/esoterica/hq9plus/                #
# https://www.dangermouse.net/esoteric/hq9plusplus.html#
# Python 3.x required                                  #
########################################################


######### IMPORTS #########
import re # RegEx for command handling
import datetime # to record script exec time
from time import sleep # for timed delays
###########################


################## DEFINITIONS ##################
def beersong():    
        for i in range (99,-1,-1):
            if i > 0:
                print(i, "bottles of beer on the wall,", i, " bottles of beer,")
                print("Take one down and pass it around,", i-1, "bottles of beer on the wall.\n")
                sleep(0.1)
            else:
                print("No more bottles of beer on the wall, no more bottles of beer.")
                print("Go to the store and buy some more, 99 bottles of beer on the wall.")
                sleep(0.5)
acm = 0

##################################################

print("PyHQ9+ Interpreter")
print("Enter a valid filename to be used as input (e.g. sample.txt)")
print("You can also drag and drop the file to this window if your terminal supports it.")
print("Make sure the file in the same folder as this script.")
print("")
while True:
    A = input()
    if A == "exit()":
            exit()
    print("")
    print("")

    # Interpreter begins here.
    begin_time = datetime.datetime.now() # Begin recording script execution time
    print("BEGIN SCRIPT")
    print("#######################################")
    print("")
    file = open(A)
    lines = file.readlines()
    for line in lines:
    
        if re.search(r'H', line): # Hello World
            B = line.count('H')
            print(B*'Hello, World! ')
        
        if re.search(r'Q', line): # Quine function
            C = line.count('Q')
            D = C * C
            print(D*'Q')

        if re.search(r'9', line): # 99 Bottles of Beer
            E = line.count('9')
            for _ in range(E):
                beersong()
                
        if '+' in line: # Increment accumulator
            F = line.count('+')
            for _ in range(F):
                    acm = acm + 1
                    print("Accumulator incremented by 1!")

        if 'P' in line: # Increment accumulator twice, initialize an object
            F = line.count('P')
            for _ in range(F):
                acm = acm + 1
                print("Accumulator incremented by 2!")
                class GenericObj:
                        obj = "GenericObject"
                print("New object instantiated.")
                        
    print("")
    print("#######################################")
    print("END SCRIPT")
    # Interpreter ends here.
    sleep(0.01)
    end_time = datetime.datetime.now() - begin_time # End recording script execution time
    print("")
    print("")
    print("Interpreter ran successfully. Script execution time below: ")
    print(end_time)
    print("")
    print("Input another filename, or type 'exit()' to exit.")
    print("")

# Version 1.1
