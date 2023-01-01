import os

cwd = os.getcwd()
data = []
with open(cwd+"/AdventOfCode/inputs/day4input.txt") as txt:
    data = txt.read().split('\n')

def cleanse(data):
    """
    Take the data, split into groups of 2;
    Take the groups of two, split each member ('-') and convert to range(a,z+1)
    """
    data = [i.split(',') for i in data if i]
    data_ranges = [
        tuple(
                _.split('-') for _ in i
            ) for i in data
    ]
    data_ranges = [tuple(list(map(int, _)) for _ in i) for i in data_ranges]
    data_ranges = [
        [range(_[0],_[1]+1) for _ in i] for i in data_ranges
    ]

    return data_ranges

def part1(data_ranges):
    """
    check for occurances of total overlap between either member of team.
    """
    _filter_func = lambda x, y: set(x).issuperset(set(y))
    x = [1 if _filter_func(i[0],i[1]) or _filter_func(i[1],i[0]) else 0 for i in data_ranges ]
    return sum(x)

def part2(data_ranges):
    """
    check for occurances of overlap between either member of team
    """
    _filter_func = lambda x, y: set(x) & set(y)
    x = [1 if _filter_func(i[0], i[1]) or _filter_func(i[1], i[0]) else 0 for i in data_ranges]
    return sum(x)


data_ranges = cleanse(data)

print(part1(data_ranges))
print(part2(data_ranges))