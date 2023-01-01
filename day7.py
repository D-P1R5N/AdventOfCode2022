import os
import json

def main():
    cwd = os.getcwd()
    data = []
    with open(cwd + "/AdventOfCode/inputs/day7input.txt") as txt:
        data = [i.rstrip('\n').split(' ') for i in txt.readlines() if i]
    return data

def test():
    test_data = """
    $ cd /
    $ ls
    1 hmm
    dir a
    $ cd a
    $ ls
    2 foo
    dir b
    dir c
    $ cd b
    $ ls
    9999999 toobig
    $ cd ..
    $ cd c
    $ ls
    30 hello
    """
    _test_data = """$ cd /
    $ ls
    dir a
    14848514 b.txt
    8504156 c.dat
    dir d
    $ cd a
    $ ls
    dir e
    29116 f
    2557 g
    62596 h.lst
    $ cd e
    $ ls
    584 i
    $ cd ..
    $ cd ..
    $ cd d
    $ ls
    4060174 j
    8033020 d.log
    5626152 d.ext
    7214296 k"""
    data = [i.split(' ') for i in _test_data.split('\n') if i]
    data = [[_ for _ in i if _] for i in data if i]
    #Annoying but important
    data = [i for i in data if i]
    return data

def create_filesystem(data):
    def pathway(path, _files):
        #This is the rabbit hole of the filesytem
        p = _files[path[0]]
        if len(path) > 1:
            for _ in path[1:]:
                p = p[_]
        return p

    def append_sizes(path, filesystem, adj=0):
        if not adj:
            return
        for p in range(len(path)):
            view = pathway(path[:p+1], filesystem)
            if not view.get("SIZE"):
                #we still do this to catch instances where
                #folders only contain other folders
                view["SIZE"] = 0
            view["SIZE"] += adj 
        return

    def create_structure(command_list):
        #Create Tree for parsing in json format
        path = []
        filesystem = {}
        filesystem['/'] = {}
        for i in data:
            if i[0] == '$':
                if i[1] == 'ls':
                    pass
                elif i[1] == 'cd':
                    if i[2] == '..':
                        #Remove last element of path, "Ascending"
                        #folder_size_adjust(path, filesystem)
                        path = path[:-1]
                        
                    else:
                        #Add path element, "Descending"
                        path.append(i[2])
        
            elif i[0] == 'dir':
                #Create folder
                view = pathway(path, filesystem)
                view[i[1]] = {}
            else:
                #add file to list, if not list, create one
                #create size key in folder
                view = pathway(path, filesystem)
                z = view.get("FILES")
                if not z:
                    z = []
                z.append((i[0],i[1]))
                view["FILES"] = z
                if not view.get("SIZE") :
                    view["SIZE"] = 0
                append_sizes(path, filesystem, adj=int(i[0]))
                
        return filesystem
    
    _filesystem = create_structure(data)
    return _filesystem

data = main()
structure = create_filesystem(data)
def part1(filesystem):
    #Find directories that are under 100000 is cumulative size
    #Add those sizes together (overlap will occur)
    def count_file_sizes(files):
        running_total = 0
        for file in files:
            temp = files[file]
            if isinstance(temp, dict):
                #dir / subdir
                _ = count_file_sizes(temp)
                if _:
                    #Don't return here
                    running_total += _
                    if running_total > 100000:
                        continue
                                                       
            elif isinstance(temp, int):
                if temp < 100000:
                    #SIZE
                    running_total += temp

                    if running_total < 100000:
                        return running_total
                    else: continue
                    
                else: 
                    pass
            
            elif isinstance(temp, list):
                #FILES
                continue
            else: pass
        #OK TO RETURN HERE
        return running_total

    size = count_file_sizes(filesystem)
    print("TOTAL " + str(size))

#print(json.dumps(structure, indent=4))
#part1(structure)
def part2(structure):
    """
    TOTAL SPACE: 70000000
    REQ. SPACE: 30000000
    ------TEST DATA------
    TOTAL SPACE: 48381165
    REQ. SPACE: 30000000
    Delete a directory to clear 8381165 of memory. 
    Find the smallest directory that can be deleted to do so
    """
    class TheCounter:
        def __init__(self, structure):
            self.filesystem = structure
            self.results = []
            self.root_size = structure["/"]["SIZE"]
            self.max_size = 70000000
            self.req_size = 30000000
            self._free = self.max_size - self.root_size
            self._placeholder = "/"
            

        def count_file_sizes(self, files=None):
            #Different than part1, uses a reqired size as metric
            if not files:
                files = self.filesystem
            running_total = 0
            for file in files:
                temp = files[file]
                
                if isinstance(temp, dict):
                    #dir / subdir
                    _ = self.count_file_sizes(files = temp)
                    if _:
                        pass                                                  
                elif isinstance(temp, int):
                    
                    if temp + self._free >= self.req_size:
                        self.results.append((temp))
                    pass
                elif isinstance(temp, list):
                    #FILES
                    continue
                else: pass
            #OK TO RETURN HERE 
            return running_total

        def tabulate(self):
            min_val = min(self.results)
            return min_val

    _ = TheCounter(structure)
    part1 = _.count_file_sizes()
    x = _.tabulate()
    print(x)
part2(structure)
    