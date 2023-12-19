with open("inputs/day14.txt") as f:
    inp = [list(l) for l in f.read().splitlines()]
    hist = ['\n'.join(''.join(l) for l in inp)]

# Part 1
def tilt_north():
    for c in range(len(inp[0])):
        r = 0
        while r < len(inp) - 1:
            if inp[r][c] == '.':
                for i in range(r + 1, len(inp)):
                    if inp[i][c] == 'O':
                        inp[r][c], inp[i][c] = 'O', '.'
                        break
                    if inp[i][c] == '#':
                        r = i
                        break
            r += 1

def calc_load():
    total = 0
    for i in range(len(inp)):
        total += len([j for j in inp[-i - 1] if j == 'O']) * (i + 1)
    return total

tilt_north()
print(calc_load())

# Part 2
def rot(l):
    return [[row[i] for row in l[::-1]] for i in range(len(l[0]))]

# Complete first cycle
for _ in range(3):
    inp = rot(inp)
    tilt_north()
inp = rot(inp)
hist.append('\n'.join(''.join(l) for l in inp))

for i in range(2, 1000000000):
    for _ in range(4):
        tilt_north()
        inp = rot(inp)
    tmp = '\n'.join(''.join(l) for l in inp)
    if tmp in hist:
        ix = hist.index(tmp)
        inp = [list(l) for l in hist[ix + ((1000000000 - ix) % (i - ix))].splitlines()]
        print(calc_load())
        break
    hist.append(tmp)