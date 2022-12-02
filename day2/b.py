import fileinput

ROCK = 1
PAPER = 2
SCISSOR = 3

LOSE = 10
DRAW = 11
WIN = 12

M = {
 "A": ROCK,
 "B": PAPER,
 "C": SCISSOR,
 "X": LOSE,
 "Y": DRAW,
 "Z": WIN
}

score = 0
for line in fileinput.input():
    if line and line != '\n':
        a, b = line.split()
        m1 = M[a]
        m2 = M[b]

        is_win = m2 == WIN

        if m2 == DRAW:
            score += m1 + 3
        elif m1 == ROCK:
            score += 6 + PAPER if is_win else SCISSOR
        elif m1 == SCISSOR:
            score += 6 + ROCK if is_win else PAPER
        else:
            score += 6 + SCISSOR if is_win else ROCK

print(score)
