import re
from math import lcm

with open("inputs/day8.txt") as f:
    inp = f.read().split("\n\n")

instrs = inp[0]
nodes = [re.findall("(.*) = \((.*), (.*)\)", l)[0] for l in inp[1].splitlines()]
lookup = dict((a, (b, c)) for a, b, c in nodes)

# Part 1
i, curr = 0, "AAA"
while curr != "ZZZ":
    curr = lookup[curr][instrs[i % len(instrs)] == 'R']
    i += 1
print(i)

# Part 2
a_nodes = [n for n in lookup.keys() if n[-1] == 'A']
res = 1
for node in a_nodes:
    count = 0
    while node[-1] != 'Z':
        node = lookup[node][instrs[count % len(instrs)] == 'R']
        count += 1
    res = lcm(res, count)
print(res)