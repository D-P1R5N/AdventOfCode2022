import os

cwd = os.getcwd()

data = []
with open(cwd+"/AdventOfCode/inputs/day5input.txt") as txt:
    data = txt.read().split('\n')
    
def data_grid(data):
    row_idx = [i for i,v in enumerate(data[8]) if v != ' ']

    data_grid = {
        k + 1 : [i[v] for i in data[:8]][::-1] for k,v in enumerate(row_idx)
    }
    data_grid = {k:[i for i in v if i!=' '] for k,v in data_grid.items()}
    return data_grid

grid = data_grid(data)
print(*grid.items(), sep='\n')
instructions = data[10:-1]
def list_restructure(instruction):
    instruction = instruction.split(' ')
    m = None
    f = None
    t = None
    print(instruction)
    for i,_ in enumerate(instruction):
        if _ == 'move':
            m = int(instruction[i+1])
        elif _ == 'from':
            f = int(instruction[i+1])
        elif _ == 'to' :
            t = int(instruction[i+1])
        else: pass

    def part1(m=int, f=int, t=int):
        #Reverse list to appear in a '1x1' fashion
        temp_reversed = grid[f][-(m):][::-1]
        grid[t] = grid[t] + temp_reversed
        grid[f] = grid[f][:-(m)]
        return

    def part2(m=int, f=int, t=int):
        #Move multiples at once
        temp = grid[f][-(m):][::]
        grid[t] = grid[t] + temp
        grid[f] = grid[f][:-(m)]
        return
    #part1(m=m,f=f,t=t)
    part2(m=m,f=f,t=t)

    return instruction

for i in instructions:
    list_restructure(i)
message = str()
for _ in grid.values():
    message += _[-1]
print(message)
"""
data_rules in 'move x from y to z' format
"""