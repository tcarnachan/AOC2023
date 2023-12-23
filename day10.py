with open("inputs/day10.txt") as f:
    inp = f.read()

start = inp.replace("\n", "").index('S')
inp = inp.splitlines()
sr, sc = divmod(start, len(inp[0]))

# Part 1
def get_adj(pos):
    row, col = pos
    N, E, S, W = (row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)
    lookup = {
        '|': [N, S],
        '-': [E, W],
        'L': [N, E],
        'J': [N, W],
        '7': [S, W],
        'F': [S, E],
        'S': [N, E, S, W],
        '.': []
    }
    return [(r, c) for r, c in lookup[inp[row][col]]
            if 0 <= r < len(inp) and 0 <= c < len(inp[0])]

loop = [(sr, sc)]
prev, curr = None, loop[0]
while True:
    next = [a for a in get_adj(curr) if curr in get_adj(a) and a != prev][0]
    if next in loop: break
    loop.append(next)
    prev, curr = curr, next
print(len(loop) // 2)

# Part 2
vertices = [(r, c) for (r, c) in loop if inp[r][c] not in '-|S']
# https://en.wikipedia.org/wiki/Shoelace_formula
area = 0
for i in range(len(vertices)):
    area += vertices[i][0] * (vertices[i - 1][1] - vertices[(i + 1) % len(vertices)][1])
area = abs(area // 2)
# https://en.wikipedia.org/wiki/Pick%27s_theorem
i = area - len(loop) // 2 + 1
print(abs(i))