import fileinput
import re

stack = []
parse_stack = True
for line in fileinput.input():
    if not parse_stack:
        m, f, t = list(map(int, re.findall(r'\d+', line)))
        for m in reversed(range(m)):
            a = stacks[f-1].pop(-1-m)
            stacks[t-1].append(a)
    elif not line or line == '\n':
        columns = list(map(int, stack[-1].split()))[-1]
        stacks = [[] for x in range(columns)]
        for s in reversed(stack[:-1]):
            for n in range(columns):
                crate = s[1 + 4*n]
                if crate.strip():
                    stacks[n].append(crate)
        parse_stack = False
    else:
        stack.append(line)

print("".join([c[-1] for c in stacks]))
