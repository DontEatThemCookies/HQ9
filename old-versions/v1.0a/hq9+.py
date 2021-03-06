#!/usr/bin/env python3

########################################################
# PyHQ9+ by David Costell, 9/25/2021                   #
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
import re # primarily needed by Quine function         #
from time import sleep # used by beer function         #
from configparser import ConfigParser # for ini        #
import os.path # for ini                               #
#                                                      #
########################################################

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
        print("Something is invalid with the ini, defaulting to case-sensitivity TRUE")
        case = True
else:
    print("No ini file found, defaulting to case-sensitivity TRUE")
    case = True

    
print("PyHQ9+ - HQ9+ Implementation for Python 3.x")
print("Case sensitivity: " + str(case))
print("")
accumulator = 0 # Pre-define the accumulator.

while True:
    A = input()

    if case == False:
        # Hello World
        if A == "h":
            print("Hello, World!")
            print("")
        # Quine function
        re.search('[q]', A) # Search for 'Q' in the input
        if re.search(r'[q]', A): # if a 'Q' was found, then
            B = len(A) # Define B as the length of the input
            C = A*B # Define C as input multiplied by length of input (A * B)
            print(C) # Print the final output
            print("")


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
        
        def beersong(x): # define song function
            if (x == 1): # if number of beer equals 1...
                beer = 'bottle' # ...change to correct singular form
                beerminus = 'bottles' # this is set to "bottles" so that "0 bottles" is shown.
            elif (x == 2): # if number of beer equals 2...
                beer = 'bottles' # ...change to correct plural form
                beerminus = 'bottle' # this is set to "bottle" so that "1 bottle" is shown.
            else: # Otherwise,
                beer = 'bottles' # set both values to plural form
                beerminus = 'bottles'

            if (x > 0): # While there's still beer...
                # ...keep singing!
                print(str(x) + " " + beer + " of beer on the wall, " + str(x) + " " + beer + " of beer.")
                print("Take one down and pass it around, " + str(x-1) + " " + beerminus + " of beer on the wall.")
                sleep(0.5)
            elif (x == 0): # Once there's no more beer...
                # ...end the song!
                print("No more bottles of beer on the wall, no more bottles of beer.")
                print("Go to the store and buy some more, 99 bottles of beer on the wall.")
                print("")
        bottles = 99 # self explanatory

        while bottles >= 0: # While there's still beer...
            beersong(bottles) # ...keep singing!
            bottles -= 1 # And subtract a bottle each time!

    # Increment the accumulator
    if A == "+":
        accumulator = accumulator + 1
        print("The accumulator has been incremented.")
        print("")

    else:
        if case == False:
            re.search('[H, h, Q, q, 9, +]', A)
            if not re.search('[H, h, Q, q, 9, +]', A):
                print("Invalid command.")
                print("")
        elif case == True:
            re.search('[H, Q, 9, +]', A)
            if not re.search(r'[H, Q, 9, +]', A):
                print("Invalid command.")
                print("")
        

        

        
        
            
# Version 1.0a
    


