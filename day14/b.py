import fileinput

size = 500
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

    last_rest = -1
    for y in range(len(grid) - 1):
        if is_blocked(cur, y+1):
            if not is_blocked(cur-1, y+1):
                cur -= 1
            elif not is_blocked(cur+1, y+1):
                cur += 1
            else:
                grid[y][cur] = 'O'
                last_rest = y
                break

    return last_rest == 0

y_max = 0
for line in fileinput.input():
    line = line.rstrip()
    coords = []
    for coord in line.split(' -> '):
        x, y = map(int, coord.split(','))
        y_max = max(y_max, y)
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

y_max += 2
for x in range(len(grid[0])):
    grid[y_max][x] = '#'

for x in range(100000):
    if simulate():
        draw()
        print(x+1)
        break
