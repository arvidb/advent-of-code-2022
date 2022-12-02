import fileinput

ROCK = 1
PAPER = 2
SCISCOR = 3

M = {
 "A": ROCK,
 "B": PAPER,
 "C": SCISCOR,
 "X": ROCK,
 "Y": PAPER,
 "Z": SCISCOR
}

score = 0
for line in fileinput.input():
    if line and line != '\n':
        a, b = line.split()
        m1 = M[a]
        m2 = M[b]

        if m1 == m2:
            score += m2 + 3
        elif (m2 is ROCK and m1 is SCISCOR) or \
             (m2 is SCISCOR and m1 is PAPER) or \
             (m2 is PAPER and m1 is ROCK):
            score += m2 + 6
        else:
            score += m2

print(score)
