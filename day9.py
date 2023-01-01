"""
Rope motion simulator
H = Head 
T = Tail
s = start poistion
. = empty node
Each motion is done in a x0, x1, x2  fashion
applying updated position to H&T respectively.
If H changes direction T does not change position,
otherwise it changes to H's previous position

PART 1: Register the number of elements the tail overlaps
"""
def part1():    
    def test_grid():
        data ="""
        ......
        ......
        ......
        ......
        H.....
        """
        grid = data.strip(' ').split('\n')
        grid = [[_ for _ in i if _ != ' '] for i in grid if i]
        return grid

    def test_rules():
        data = """R 4
            U 4
            L 3
            D 1
            R 4
            D 1
            L 5
            R 2"""
        rules = data.split("\n")
        rules = [i.strip().split(' ') for i in rules if i]
        return rules

    def main_rules():
        import os
        cwd = os.getcwd()
        with open(cwd + "/AdventOfCode/inputs/day9input.txt") as txt:
            data = txt.read().split('\n')[:-1]
        data = [i.split(' ') for i in data]
        return data

    class Grid:
        def __init__(self, grid):
            self.grid = grid
            self.rules = []
            self.start = self.find_rope(grid)
            self.last_direction = ''
            self.head_current = self.start
            self.head_previous = (0,0)
            self.tail_current = self.start
            self.tail_previous = (0,0)
            self.tail_locations = set(self.tail_current)
            #tail locations will be a set
        
        def __str__(self):
            return '\n'.join((str(i) for i in self.grid))

        def find_rope(self, grid, indicator = 'H'):
            # y , x [row_idx], [col_idx]
            for row, x in enumerate(grid):
                for col, y in enumerate(x):
                    if y == indicator:
                        return (row, col)
            return (0,0)

        def register(self, rules):
            self.rules = rules
            return rules

        def interpret(self):
            grid = self.grid
            
            for rule in self.rules:
                h = self.update_head(rule[0], rule[1])
            return
        
        def update_tail(self):
            t_x, t_y = self.tail_current
            h_x, h_y = self.head_current
            if any([
                (abs(h_x-t_x) > 1),
                (abs(h_y - t_y) > 1)
            ]):
                self.tail_current = self.head_previous
                self.tail_locations.add(self.tail_current)
                
            else:
                pass
        
        def update_head(self, direction, value):
            i_row, i_col = self.head_current
            print(i_row, i_col)
            _r = range(int(value))
            for _ in _r:
                self.head_previous = self.head_current
                if direction == "R":
                    self.head_current = (
                        self.head_current[0], 
                        self.head_current[1] + 1
                        )
                elif direction == "L":
                    self.head_current = (
                        self.head_current[0], 
                        self.head_current[1] - 1
                    )
                elif direction == "U":
                    self.head_current = (
                        self.head_current[0] - 1,
                        self.head_current[1]
                    )
                elif direction == "D":
                    self.head_current = (
                        self.head_current[0] + 1,
                        self.head_current[1]
                    )
                else:
                    print(direction, value)
                self.update_tail()        
            return 

    obj = Grid(test_grid())
    obj.register(main_rules())
    obj.interpret()
    print(obj.tail_locations)
    #We add 1 to the length of known tail locations

def part2():
    #simulate the same motions as before
    #except on 10 nodes instead of 2
    #Same rules apply (if 9 is too far away from 8, etc...)
    def main_grid():
        data = """
        ..........................
        ..........................
        ..........................
        ..........................
        ..........................
        ..........................
        ..........................
        ..........................
        ..........................
        ..........................
        ..........................
        ..........................
        ..........................
        ..........................
        ..........................
        ...........H..............
        ..........................
        ..........................
        ..........................
        ..........................
        ..........................
        """
        grid = data.strip(' ').split('\n')
        grid = [[_ for _ in i if _ != ' '] for i in grid if i]
        return grid
    
    def test_rules():
        data = """R 4
            U 4
            L 3
            D 1
            R 4
            D 1
            L 5
            R 2"""
        rules = data.split("\n")
        rules = [i.strip().split(' ') for i in rules if i]
        return rules

    def main_rules():
        import os
        cwd = os.getcwd()
        with open(cwd + "/AdventOfCode/inputs/day9input.txt") as txt:
            data = txt.read().split('\n')[:-1]
        data = [i.split(' ') for i in data]
        return data
    class Rope:
        class Knot:
            def __init__(self, id):
                self.id = id
                self.position = (0,0)
                self.previous = (0,0)

            def __str__(self):
                return str(self.id)
            
            def move_required(self, prev):
                if not isinstance(prev, Rope.Knot):
                    raise ValueError(f"{repr(prev)} is not a Knot")
                k1_x, k1_y = self.position
                k2_x, k2_y = prev.position
                if any([
                        (abs(k2_x-k1_x) > 1),
                        (abs(k2_y-k1_y) > 1)
                    ]):
                    return True
                else:
                    return False

            def move(self, direction):
                self.previous = self.position
                if direction == "R":
                    self.head_current = (
                        self.position[0], 
                        self.position[1] + 1
                        )
                elif direction == "L":
                    self.position = (
                        self.position[0], 
                        self.position[1] - 1
                    )
                elif direction == "U":
                    self.position = (
                        self.position[0] - 1,
                        self.position[1]
                    )
                elif direction == "D":
                    self.position = (
                        self.position[0] + 1,
                        self.position[1]
                    )
                else:
                    #Just in case?
                    pass
                return 

        class Tail(Knot):
            def __init__(self, id):
                super().__init__(id)
                self.history = set()
                self.history.add(self.position)
            def __repr__(self):
                return "This is the tail"
            def move_required(self, prev):
                return super().move_required(prev)
            def move(self, direction):
                super().move(direction)
                self.history.add(self.position)
                return

        def __init__(self, nodes):
            self.length = nodes
            self.origin = (0,0)
            self._i = 0
            self.knots = self.create_nodes(nodes)
            self.tail = self.knots[-1]
        def __iter__(self):
            return self
        
        def __next__(self):
            if self._i> self.length - 1:
                raise StopIteration
            else:
                self._i += 1
                return self.knots[self._i - 1]

        def set_origin(self, grid):
            for row, x in enumerate(grid):
                for col, y in enumerate(x):
                    if y == 'H':
                        return (row, col)
            return (0,0)

        def create_nodes(self, nodes):
            node_list = []
            node_list = [
                Rope.Knot(i) if i!= self.length - 1 else Rope.Tail(i) for i in range(nodes)
                ]
            return node_list

        def translate(self, movement):
            direction, distance = movement
            for r in range(int(distance)):
                
                for knot in self.knots:
                    if knot.id == 0:
                        knot.move(direction)
                    else:
                        if knot.move_required(self.knots[knot.id-1]):
                            knot.move(direction)
                        else:
                            pass
            return
    movements = main_rules()
    grid = main_grid()
    rope = Rope(10)
    rope.set_origin(grid)
    for move in movements:
        rope.translate(move)
    print(len(rope.tail.history))
    for knot in rope:
        print(knot.position)
part2()
