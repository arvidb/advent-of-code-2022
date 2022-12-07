import fileinput

class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.dirs = []
        self.files = []

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

root = Directory("/")
cur = root
for line in fileinput.input():
    line = line.rstrip('\n')
    if line.startswith("$ ls"):
        continue
    elif line.startswith("$ cd"):
        target_dir = line.split()[-1]
        if target_dir == "..":
            cur = cur.parent
        else:
            for d in cur.dirs:
                if d.name == target_dir:
                    cur = d
    elif line.startswith("dir"):
        name = line.split()[-1]
        cur.dirs.append(Directory(name, cur))
    else:
        # File
        size, name = line.split()
        cur.files.append(File(name, int(size)))


sizes = []
def calc_size(cur_dir, lim):
    size = 0
    size += sum([calc_size(d, lim) for d in cur_dir.dirs])
    size += sum([f.size for f in cur_dir.files])
    if lim != None and size > lim:
        sizes.append(size)
    return size

tot = calc_size(root, None)
calc_size(root, tot - 40000000)
print(min(sizes))
