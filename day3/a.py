import fileinput

prio = 0
for line in fileinput.input():
    if line and line != '\n':
        a, b = line[:len(line)//2], line[len(line)//2:]
        AB = set(a) & set(b)
        for c in AB:
            if c.isupper():
                prio += ord(c) - ord('A') + 27
            else:
                prio += ord(c) - ord('a') + 1

print(prio)
