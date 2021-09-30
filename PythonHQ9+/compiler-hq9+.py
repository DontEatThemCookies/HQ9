#!/usr/bin/env python3

########################################################
# PyHQ9+ Compiler by David Costell, 9/29/2021          #
# Python implementation of the esoteric language HQ9+  #
# "Compiles" a Python3 file from HQ9+ user input.      #
# Original HQ9+ concept by Cliff L. Biffle, 2001       #
#                                                      #
# Learn more about HQ9+ here:                          #
# http://cliffle.com/esoterica/hq9plus/                #
# Python 3.x required                                  #
########################################################

# Disclaimer: This is a BETA release of the PyHQ9+ compiler.
# Optimizations and/or cleanliness not guaranteed for this release.
# Currently, this compiler is a PROOF-OF-CONCEPT.
# Refactoring is expected on one of the final release candidates.

######### IMPORTS #########
import os # for exception catching
import sys # for exception catching
import datetime # to record exec time
import inspect # for 99 bottles
from time import sleep # for timed delays
###########################


################## DEFINITIONS ##################
def beersong():    
        for i in range (99,-1,-1): # 99 Bottles of Beer            
            if i > 2:
                print(i, "bottles of beer on the wall,", i, " bottles of beer,")
                print("Take one down and pass it around,", i-1, "bottles of beer on the wall.\n")
                
            elif i == 2:
                    print(i, "bottles of beer on the wall,", i, " bottles of beer,")
                    print("Take one down and pass it around,", i-1, "bottle of beer on the wall.\n")
            elif i == 1:
                    print(i, "bottle of beer on the wall,", i, " bottle of beer,")
                    print("Take one down and pass it around,", i-1, "bottles of beer on the wall.\n")
            else:
                print("No more bottles of beer on the wall, no more bottles of beer.")
                print("Go to the store and buy some more, 99 bottles of beer on the wall.")
                
'''Pre-defines the commands to be written to file
Needed to prevent NameErrors (prints blank line if that certain var wasn't called)'''
h = ""
h1 = ""
q = ""
q1 = ""
q2 = ""
nine = ""
prenine1 = ""
prenine2 = ""
p = ""
p1 = ""
p2 = ""
p3 = ""
linux = "#!/usr/bin/env python3 \n"
header = "#Compiled by the PyHQ9+ Compiler (Python 3) - "+str(datetime.datetime.now())
n = " \n" # Newline

acm = 0 # Accumulator
acm2 = "acm = 0 # Accumulator"+n

##################################################

print("PyHQ9+ Compiler")
print("Compiles HQ9+ into Python 3 code.")
print("Input the necessary info to begin compilation.")
print("NOTE: The output file will be written to the same directory as this compiler.")
print("")

name = input("Name the file (e.g. myhq9program): ")
print("")

A = input("Input commands [valid: H, Q, 9, +]: ")
begin = datetime.datetime.now()
print("BEGIN COMPILE")
print("#######################################")

# Compiler

A1 = "A = '"+str(A)+"'"
fnl = "input('Press any key to continue...')"

try:
        filename = name+".py"
        with open(filename, 'x') as f:
                
                if 'H' in A: # Hello, World!
                        h1 = "H = A.count('H') # Hello World"
                        h = "print(H*'Hello, World! ') \n"

                if 'Q' in A: # The quine function
                        q1 = "q1 = A.count('Q') # Quine function"
                        q2 = "q2 = q1 * q1"
                        q = "print(q2*'Q') \n"
                    
                if '9' in A: # 99 Bottles of Beer
                        prenine1 = inspect.getsource(beersong)
                        prenine2 = "beersong()"+n
                        nine = prenine1+prenine2+n
                
                if '+' in A: # Accumulator
                        p = "acmc = A.count('+') # Accumulator"
                        p1 = "for _ in range(acmc):"
                        p2 = "    acm = acm + 1"
                        p3 = "    print('Accumulator has been incremented!') \n"

                writeoutput = linux+header+n+A1+n+acm2+n+h1+n+h+n+q1+n+q2+n+q+n+nine+p+n+p1+n+p2+n+p3+n+fnl
                # Spaghetti code - will be optimized soon
                
                f.write(writeoutput)
                
             

except FileExistsError:
        print("An error occurred while attempting compile!")
        print("Error: File already exists with the same name -", sys.exc_info()[0])
        e = input("Would you like to remove the file? (Irreversible!) [Y/N] ")
        if e == "Y":
                os.remove(filename)
                print("File deleted.")
                sleep(2)
                exit()
        elif e == "N":
                print("File preserved.")
                sleep(2)
                exit()
        else:
                exit()
                
except NameError:
        pass
        
except: # for other errors
        print("An error occurred while attempting compile!")
        print("Specific error: ", sys.exc_info()[0])
        os.remove(filename)
        sleep(5)

print("END COMPILE")
print("The code has compiled successfully.")
print("File compiled as: "+filename)
sleep(0.00001)
endtime = datetime.datetime.now() - begin
print(endtime)
sleep(3)

# Beta 2
