import fileinput

total = 0
for line in fileinput.input():
    a, b = line.split(',')
    a = tuple(map(int, a.split('-')))
    b = tuple(map(int, b.split('-')))
    
    a = set(range(a[0], 1+a[1]))
    b = set(range(b[0], 1+b[1]))

    if len(set(a) & set(b)) == len(b if len(a) > len(b) else a):
        total += 1

print(total)
