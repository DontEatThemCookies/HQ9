# This is a sample output file from the transcompiler.

#!/usr/bin/env python3

# Transcompiled to Python 3 by the Phoenix Engine
# Compiled 12/09/2021, 19:08:33

line = 'HQQQQ+'
accumulator = 0

for _ in range(line.upper().count("H")):
    print("Hello, World!")

for _ in range(line.upper().count("Q")):
    print("Q" * line.upper().count("Q"))

for _ in range(line.count("+")):
    accumulator += 1

input()
