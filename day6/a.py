import fileinput

tmp = []
for i,  c in enumerate(next(fileinput.input())):
    if len(tmp) == 4:
        if len(set(tmp)) == 4:
            print(i)
        else:
            tmp.pop(0)
    tmp.append(c)


