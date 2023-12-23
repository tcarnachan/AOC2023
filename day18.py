with open("inputs/day18.txt") as f:
    inp = f.read().splitlines()

dirs = { 'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0) }

def get_area(parse):
    vertices = [[0, 0]]
    pos = [0, 0]
    length = 0
    for line in inp:
        dir, dist = parse(line)
        length += dist
        pos[0] += dir[0] * dist
        pos[1] += dir[1] * dist
        vertices.append(list(pos))

    area = 0
    for i in range(len(vertices)):
        area += vertices[i][0] * (vertices[i - 1][1] - vertices[(i + 1) % len(vertices)][1])
    area = abs(area // 2)
    return abs(area - length // 2 + 1) + length

# Part 1
def parse1(line):
    dir, dist, _ = line.split()
    return (dirs[dir], int(dist))
print(get_area(parse1))

# Part 2
def parse2(line):
    _, _, hx = line.split()
    return (dirs['RDLU'[int(hx[-2])]], int(hx[2:-2], 16))
print(get_area(parse2))