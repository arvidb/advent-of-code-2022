import fileinput

rows = []
for line in fileinput.input():
    line = line.rstrip('\n')
    row = [int(c) for c in line]
    rows.append(row)


n_rows = len(rows)
n_cols = len(rows[0])

def count_visibility(x, y):
    left = [rows[y][i] for i in reversed(range(x))]
    right = [rows[y][i] for i in range(x+1, n_cols)]
    up = [rows[i][x] for i in reversed(range(y))]
    down = [rows[i][x] for i in range(y+1, n_rows)]
   
    tot = 1
    num = rows[y][x]
    for d in [left, right, up, down]:
        c = 0
        for i in d:
            c += 1
            if i >= num:
                break
        tot *= c
    
    return tot

best = 0
for x in range(1, n_cols-1):
    for y in range(1, n_rows-1):
        best = max(best, count_visibility(x, y))

print(best)
