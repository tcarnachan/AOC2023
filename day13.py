with open("inputs/day13.txt") as f:
    inp = f.read().split('\n\n')

def is_reflection(rows):
    return len(rows) > 0 and len(rows) % 2 == 0 and rows[:(i := len(rows) // 2)] == rows[i:][::-1]

# Part 1
def find_reflections(rows):
    refls = []
    for i in range(len(rows) - 1):
        if is_reflection(rows[i:]):
            refls.append(i + len(rows[i:]) // 2)
        if is_reflection(rows[:-i - 1]):
            refls.append(len(rows[:-i - 1]) // 2)
    return refls

refl_lines = []
for pattern in inp:
    rows = pattern.splitlines()
    if t := find_reflections(rows):
        refl_lines.append(t[0] * 100)
    else:
        cols = [''.join(r[i] for r in rows[::-1]) for i in range(len(rows[0]))]
        refl_lines.append(find_reflections(cols)[0])
print(sum(refl_lines))

# Part 2
total = 0
for ix, pattern in enumerate(inp):
    rows = [list(l) for l in pattern.splitlines()]

    for i in range(len(rows) * len(rows[0])):
        r, c = divmod(i, len(rows[0]))
        rows[r][c] = '.#'[rows[r][c] == '#']

        if (t := [i for i in find_reflections(rows) if i * 100 != refl_lines[ix]]):
            total += t[0] * 100
            break

        cols = [''.join(r[i] for r in rows[::-1]) for i in range(len(rows[0]))]
        if (t := [i for i in find_reflections(cols) if i != refl_lines[ix]]):
            total += t[0]
            break

        rows[r][c] = '.#'[rows[r][c] == '#']
print(total)