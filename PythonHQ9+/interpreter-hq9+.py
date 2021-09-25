#!/usr/bin/env python3

########################################################
# PyHQ9+ Interpreter by David Costell, 9/25/2021       #
# Python implementation of the esoteric language HQ9+  #
# Interprets commands from a file instead of a shell.  #
# Original HQ9+ concept by Cliff L. Biffle, 2001       #
#                                                      #
# Learn more about HQ9+ here:                          #
# http://cliffle.com/esoterica/hq9plus/                #
# Python 3.x required                                  #
########################################################


######### IMPORTS #########
import re 
from time import sleep
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


print("Enter a valid filename to be used as input (e.g. sample.txt)")
print("You can also drag and drop the file to this window in Windows 10.")
print("Make sure the file in the same folder as this script.")
print("Operations will be executed based on the order they are sorted in the file.")
print("")
while True:
    A = input()
    print("")

    # Interpreter begins here.
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
        if re.search(r'P', line): # Increase the accumulator
            F = line.count('P')
            for _ in range(F):
                acm = acm + 1
                print("Accumulator incremented by 1!")
            
    # Interpreter ends here.

    print("")
    print("Interpreter ran successfully.")
    print("Input another filename, or type 'exit()' to exit.")
    Z = input()
    if Z == "exit()":
            exit()

# Version 1
