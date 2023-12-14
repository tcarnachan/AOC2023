with open("inputs/day9.txt") as f:
    inp = f.readlines()

def calc_hist(line, ix):
    hist = [line]
    while any(x != 0 for x in line):
        line = [b - a for a, b in zip(line, line[1:])]
        hist.append(line)
    for i in range(len(hist) - 2, -1, -1):
        hist[i][ix] += hist[i + 1][ix] * (ix * -2 - 1)
    return hist[0][ix]

s, s2 = 0, 0
for line in inp:
    line = [int(i) for i in line.split()]
    s += calc_hist(list(line), -1)
    s2 += calc_hist(line, 0)
print(s)
print(s2)