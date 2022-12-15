import fileinput

size = 200
mid = 500

grid = [['.' for _ in range(size)] for _ in range(size)]

def draw():
    for row in range(len(grid)):
        print(row, end='')
        for col in range(len(grid[row])):
            print(grid[row][col], end='')
        print()

def simulate():
    cur = mid - (mid - size//2)
    grid[0][cur] = '+'

    def is_blocked(x, y):
        return grid[y][x] == '#' or grid[y][x] == 'O'

    placed = False
    for y in range(len(grid) - 1):
        if is_blocked(cur, y+1):
            if not is_blocked(cur-1, y+1):
                cur -= 1
            elif not is_blocked(cur+1, y+1):
                cur += 1
            else:
                grid[y][cur] = 'O'
                placed = True
                break
    return placed

for line in fileinput.input():
    line = line.rstrip()
    coords = []
    for coord in line.split(' -> '):
        x, y = map(int, coord.split(','))
        x = x - (mid - size//2)
        coords.append((x, y))
    for idx in range(1, len(coords)):
        x1, y1 = coords[idx-1]
        x2, y2 = coords[idx]
        ylen = abs(y1-y2)
        xlen = abs(x1-x2)
        for y in range(ylen+1):
            for x in range(xlen+1):
                x0 = x + min(x1, x2)
                y0 = y + min(y1, y2)
                grid[y0][x0] = '#'

for x in range(1000):
    if not simulate():
        draw()
        print(x)
        break
