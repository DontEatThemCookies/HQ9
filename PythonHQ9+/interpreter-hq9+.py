#!/usr/bin/env python3

########################################################
# PyHQ9+ Interpreter by David Costell, 9/30/2021       #
# Python implementation of the esoteric language HQ9+  #
# Interprets commands from a file instead of a shell.  #
# Original HQ9+ concept by Cliff L. Biffle, 2001       #
#                                                      #
# Learn more about HQ9+ here:                          #
# http://cliffle.com/esoterica/hq9plus/                #
# Python 3.x required                                  #
########################################################

######### IMPORTS #########
import datetime # to record script exec time
from time import sleep # for timed delays
###########################


################## DEFINITIONS ##################
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
acm = 0

##################################################

# Initialization

print("PyHQ9+ Interpreter v1.1")
print("")
print("Enter a path to a file/filename to be interpreted (e.g. input.txt or C:\input.txt)")
print("You can also drag and drop the file to this window if your terminal supports it.")
print("If you only input a filename, ensure the file is in the same folder as this interpreter.")
print("")

while True:
    A = input()
    if A == "exit()":
            exit()
    print("")
    print("")

    # Interpreter begins here.
    begin_time = datetime.datetime.now() # Begin recording script execution time
    print("BEGIN EXECUTION")
    print("#######################################")
    print("")
    file = open(A)
    lines = file.readlines()
    for line in lines:
        
        if 'H' in line: # Hello World
                B = line.count('H')
                print(B*'Hello, World! ')

        if 'Q' in line: # Quine function
                C = line.count('Q')
                D = C * C
                print(D*'Q')

        if '9' in line: # 99 Bottles of Beer
                E = line.count('9')
                for _ in range(E):
                        beersong()
                
        if '+' in line:
                F = line.count('+')
                for _ in range(F):
                        acm = acm + 1
                        print("Accumulator incremented by 1!")
    print("")
    print("#######################################")
    print("END OF FILE")
    # Interpreter ends here.
    sleep(0.00001)
    end_time = datetime.datetime.now() - begin_time # End recording script execution time
    print("")
    print("")
    print("Interpreter ran successfully. Script execution time below: ")
    print(end_time)
    print("")
    print("Input another filename, or type 'exit()' to exit.")
    print("")

# Version 1.1a
