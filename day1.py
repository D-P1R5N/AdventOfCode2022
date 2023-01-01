import os

def results(data):
    final = []
    sub = []
    for _ in data:
        if len(_) > 0:
            sub.append(int(_))
        elif len(_) == 0:
            final.append(sub)
            sub = []
    
    return final

def find_max(results):
    max = 0
    for _ in results:
        if _ > max: 
            max = _
        else:
            pass
    return max
print(os.listdir(os.getcwd()))
data = []
with open(".\AdventOfCode\day1input.txt") as txt:
    data = txt.read().split('\n')
_data = results(data)
_data = [sum(i) for i in _data]
max = find_max(_data)

#day 1 challenge 2, find top 3 values in
_data.sort(reverse=True)
print(sum(_data[:3]))