# Sample output of Phoenix transcompiler

#!/usr/bin/env python3

# Compiled 01/27/2022, 19:46:22

line = 'HQQQQ+'
accumulator = 0

for _ in range(line.upper().count("H")):
    print("Hello, World!")

for _ in range(line.upper().count("Q")):
    print("Q" * line.upper().count("Q"))

for _ in range(line.count("+")):
    accumulator += 1

input()
