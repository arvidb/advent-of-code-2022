import fileinput

rows = []
for line in fileinput.input():
    line = line.rstrip('\n')
    row = [int(c) for c in line]
    rows.append(row)


n_rows = len(rows)
n_cols = len(rows[0])

def is_visible(x, y):
    left = [rows[y][i] for i in reversed(range(x))]
    right = [rows[y][i] for i in range(x+1, n_cols)]
    up = [rows[i][x] for i in reversed(range(y))]
    down = [rows[i][x] for i in range(y+1, n_rows)]
  
    num = rows[y][x]
    for d in [left, right, up, down]:
        if all(i < num for i in d):
            return True
    
    return False

tot = 0
for x in range(1, n_cols-1):
    for y in range(1, n_rows-1):
        tot += 1 if is_visible(x, y) else 0

print(2*n_rows + 2*(n_cols - 2) + tot)
