import os

cwd = os.getcwd()
data = str()
with open(cwd + "/AdventOfCode/inputs/day6input.txt") as txt:
    data = txt.read()

print(data)
"""
Find a unique sequence of charachters in a given string
Sets consume less memory because there is no indexing,
making them useful for larger operations where position
doesn't matter
"""
def part1(data):
    #Sequence length 4
    for i, v in enumerate(data):
        if len(set(data[i:i+4])) < 4:
            continue
        else:
            return i + 4

def part2(data):
    #Sequence length 14
    for i, v in enumerate(data):
        if len(set(data[i:i+14])) < 14:
            continue
        else:
            return i + 14
    
print(part2(data))
