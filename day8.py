"""
Generate a topographical map from number sequences; get number of
visible elements from container edges, where there are no elements
between that element and an edge that are greater in value than the 
current element
"""
import os
def test():
    t = """
    30373
    25512
    65332
    33549
    35390
    """
    #removes leading and trailing empty elements due to above styling
    data = [list(i.strip(' ')) for i in t.split("\n")[1:-1]]
    data = [list(map(int, i)) for i in data]
    return data

def main():
    cwd = os.getcwd()
    with open(cwd +"/AdventOfCode/inputs/day8input.txt") as txt:
        data = list(map(lambda x : x.strip('\n'), txt.readlines()))
        data = [list(map(int, list(i))) for i in data]
        return data
def part1(data):
    """
    Descend deeper into the matrix by checking elements
    -> Probably easiest to find the 
    """
    """mask_arr = []
    #We look at each element in a row. 
    mask_x  = 0
    mask_row = []
    for idx_x, row in enumerate(data):
        for idx_y, col in enumerate(row):
            mask_col = [i[idx_y] for i in data]
            print(mask_col)
            pass"""
    mask_arr = []
    func = lambda x, y: x < y
    for i_x,row in enumerate(data):
        mask_row = []
        print(i_x)
        for i_y,col in enumerate(row):
            mask_col = [i[i_y] for i in data]
            #Edge cases are automatically visible
            if any([
                (i_x == 0),
                (i_x == len(row)-1),
                (i_y == 0),
                (i_y == len(data)-1)
            ]):
                mask_row.append(True)
                continue
            
            if any([
                #check for visibility from top:
                all(map(lambda x: x < col, mask_col[:i_x])),
                #check for visibility from bottom:
                all(map(lambda x: x < col, mask_col[i_x+1:])),
                #check for visibility from left:
                all(map(lambda x: x < col, row[i_y+1:])),
                #check for visibility from right:
                all(map(lambda x: x < col, row[:i_y]))

                ]):
                    mask_row.append(True)
            else:
                mask_row.append(False)
        mask_arr.append(mask_row)

    def sum_it(arr):
        s = 0
        for _ in arr:
            s += sum([1 if t else 0 for t in _])
        return s
    return sum_it(mask_arr)
#x = part1(main())
#print(*x, sep='\n')

def part2(data):
    """
    For each individual column element, determin it's scenic score;
    the scenic score is  L*R*U*D in terms of relative distance to :
    a) edge
    b) higher value column element
    Get highest value possible
    test values : ->
        Element : 2 , 3 (row 4, col 3)
            Score = 8
    """
    data = data
    high_score = 0
    def scenic_score(y_idx, x_idx):
        #x_idx will give element in row
        #y_idx will give row in data
        def s_left(row, position):
            if position == 0:
                return 0
            else:
                #but not including, position
                left_reversed = row[:position][::-1]
                current = row[position]
                #we reverse to take the first occurance
                #of a larger value
                for i,v in enumerate(left_reversed):
                    if v >= current:
                        return i+1
                return position
        def s_right(row, position):
            #edge case
            if position == len(row) - 1:
                return 0
            else:
                right = row[position+1:]
                current = row[position]
                for i,v in enumerate(right):
                    #we return at the first occurance of
                    #higher value
                    if v >= current:
                        return i + 1
                #Can see full row away
                return len(right)
        def s_up(col, position):
            if position == 0:
                #top row of column
                return 0
            else:
                up = col[:position][::-1]
                current = col[position]
                for i,v in enumerate(up):
                    if v>=current:
                        return i+1
                return position
        def s_down(col, position):
            if position == len(col)-1:
                return 0
            else:
                down = col[position+1:]
                current = col[position]
                for i,v in enumerate(down):
                    if v >= current:
                        return i + 1       
                return len(down)
        row = data[y_idx]
        col = [i[x_idx] for i in data]
        s = 0 
        l = s_left(row, x_idx)
        r = s_right(row, x_idx)
        u = s_up(col, y_idx)
        d = s_down(col, y_idx)
        
        s = u * l * d * r
        return s
    for row_i, row in enumerate(data):
        for col_i, col in enumerate(row):
            score = scenic_score(row_i, col_i)
            if score > high_score:
                high_score = score
            pass

    return high_score
print(part2(main()))
