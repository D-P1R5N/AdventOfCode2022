import os
import string

cwd = os.getcwd()
CHAR = {v : k+1 for k,v in enumerate(string.ascii_letters)}
data = []
with open(cwd + "/AdventOfCode/inputs/day3input.txt") as txt:
    data = txt.read().split('\n')
    #data = [list(i) for i in data if i]

def part1(data):
    """Find the common item type between two compartments for each rucksack.
        Divide the bag in half, find the unique items (no duplicates necessary),
        Then check for common elements between those two sets."""
    data = [
            [set(i[0:(len(i)//2)]) , set(i[len(i)//2:])] for i in data if i
        ]

    common = [(i[0] & i[1]) for i in data]
    common_sum = 0
    for _ in common:
        common_sum += CHAR[_.pop()]
    return common_sum
#print(part1(data))

def part2(data):
    """Group data into groups of 3 members, find common item between each member"""
    data = [
        data[i:i+3] for i in range(0, len(data), 3)
    ][:-1]
    data = [[set(i) for i in _] for _ in data]
    print(data)
    common = [(i[0]&i[1]&i[2]) for i in data]
    common_sum = 0
    for _ in common:
        common_sum += CHAR[_.pop()]
    return common_sum
print(part2(data))