import re

with open("inputs/day2.txt") as f:
    inp = f.readlines()

s = 0
colours = [("red", 12), ("green", 13), ("blue", 14)]
for line in inp:
    possible = True
    for colour, num in colours:
        t = max([int(i) for i in re.findall(f"(\d+) {colour}", line)])
        possible &= t <= num
    if possible:
        s += int(re.findall("Game (\d+)", line)[0])
print(s)

s = 0
for line in inp:
    power = 1
    for colour, _ in colours:
        power *= max([int(i) for i in re.findall(f"(\d+) {colour}", line)])
    s += power
print(s)