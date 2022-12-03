import fileinput

prio = 0
group = []
for line in fileinput.input():
    if line and line != '\n':
        group.append(line.rstrip())

    if len(group) == 3:
        ABC = set(group[0]) & set(group[1]) & set(group[2])
        group = []
        for c in ABC:
            if c.isupper():
                prio += ord(c) - ord('A') + 27
            else:
                prio += ord(c) - ord('a') + 1

print(prio)
