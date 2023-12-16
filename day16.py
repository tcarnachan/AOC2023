with open("inputs/day16.txt") as f:
    inp = f.read().splitlines()

UP, LEFT, DOWN, RIGHT = 0, 1, 2, 3
dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def add(x, y): return (x[0] + y[0], x[1] + y[1])

light = [((0, 0), RIGHT)]

def count_energized(start, dir):
    light = [(start, dir)]
    energized = set()
    seen = [[set() for _ in range(len(inp[0]))] for _ in range(len(inp))]

    while len(light) > 0:
        curr, dir = light.pop(0)
        r, c = curr
        if r < 0 or r > len(inp) - 1 or c < 0 or c > len(inp[0]) - 1 or dir in seen[r][c]:
            continue
        seen[r][c].add(dir)
        energized.add(curr)

        if inp[r][c] == '/':
            # Right <-> Up, Left <-> Down; 3 <-> 0, 1 <-> 2
            dir = 3 - dir
        elif inp[r][c] == '\\':
            # Right <-> Down, Left <-> Up; 3 <-> 2; 1 <-> 0
            dir += [1, -1][dir % 2]
        else:
            if inp[r][c] == '|' and (dir == LEFT or dir == RIGHT):
                light.append((add(curr, dirs[UP]), UP))
                dir = DOWN
            if inp[r][c] == '-' and (dir == UP or dir == DOWN):
                light.append((add(curr, dirs[LEFT]), LEFT))
                dir = RIGHT

        light.append((add(curr, dirs[dir]), dir))
    return len(energized)

# Part 1
print(count_energized((0, 0), RIGHT))

# Part 2
m = 0
for i in range(len(inp[0])):
    m = max(m,
            count_energized((0, i), DOWN),
            count_energized((len(inp) - 1, i), UP))
for i in range(len(inp)):
    m = max(m,
            count_energized((i, 0), RIGHT),
            count_energized((i, len(inp[0]) - 1), LEFT))
print(m)