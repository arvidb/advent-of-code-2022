import fileinput

cals = []
calories = 0
for line in fileinput.input():
    if line and line != '\n':
        calories += int(line)
    else:
        cals.append(calories)
        calories = 0

cals.sort(reverse=True)
print(sum(cals[:3]))
