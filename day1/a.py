import fileinput

max_calories = 0
calories = 0
for line in fileinput.input(encoding="utf-8"):
    if line and line != '\n':
        calories += int(line)
    else:
        max_calories = max(max_calories, calories)
        calories = 0

print(max_calories)
