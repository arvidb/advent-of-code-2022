import fileinput

tmp = []
for i,  c in enumerate(next(fileinput.input())):
    if len(tmp) == 14:
        if len(set(tmp)) == 14:
            print(i)
        else:
            tmp.pop(0)
    tmp.append(c)


