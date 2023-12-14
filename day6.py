from math import sqrt, ceil

with open("inputs/day6.txt") as f:
    inp = f.readlines()

def get_ways(t, d):
    disc = sqrt(t * t - 4 * d)
    t1, t2 = .5 * (t - disc), .5 * (t + disc)
    return ceil(t2) - int(t1 + 1)

# Part 1
total = 1
for t, d in list(zip(inp[0].split(), inp[1].split()))[1:]:
    total *= get_ways(int(t), int(d))
print(total)

# Part 2
t, d = [int("".join(l.split()[1:])) for l in inp]
print(get_ways(t, d))