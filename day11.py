from itertools import product

with open("inputs/day11.txt") as f:
    inp = list(map(list, f.read().splitlines()))

cols, rows = len(inp[0]), len(inp)

empty_rows = [r for r in range(rows) if all(c == '.' for c in inp[r])]
empty_cols = [c for c in range(cols) if all(inp[r][c] == '.' for r in range(rows))]

galaxies = [(r, c) for (r, c) in product(range(rows), range(cols)) if inp[r][c] == '#']

def get_dists(empty_len):
    s = 0
    for i, e in enumerate(galaxies):
        for g in galaxies[i+1:]:
            (r1, c1), (r2, c2) = e, g
            if r1 > r2: r1, r2 = r2, r1
            if c1 > c2: c1, c2 = c2, c1
            e_rows = len([r for r in empty_rows if r1 < r < r2])
            e_cols = len([c for c in empty_cols if c1 < c < c2])
            s += r2 - r1 + c2 - c1 + (e_rows + e_cols) * (empty_len - 1)
    return s

# Part 1
print(get_dists(2))

# Part 2:
print(get_dists(1000000))