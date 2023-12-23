with open("inputs/day5.txt") as f:
    inp = f.read().split("\n\n")

seeds = [int(s) for s in inp[0].split(' ')[1:]]

maps = []
for i in range(1, len(inp)):
    maps.append([[int(n) for n in r.split()]
                 for r in inp[i].splitlines()[1:]])

# Part 1
locations = []
for seed in seeds:
    tmp = seed
    for map in maps:
        for dest, src, ln in map:
            if src <= tmp <= src + ln:
                tmp += dest - src
                break
    locations.append(tmp)
print(min(locations))

# Part 2
ranges = []
for i in range(0, len(seeds), 2):
    ranges.append((seeds[i], seeds[i] + seeds[i + 1] - 1))

# Returns range1 in the form [overlap, range1 lower than overlap, range1 higher than overlap]
def split_by_overlap(range1, range2):
    a1, b1 = range1
    a2, b2 = range2

    # No overlap
    if a1 > b2 or a2 > b1: return None

    # Overlap
    overlap = (max(a1, a2), min(b1, b2))
    lower = (a1, overlap[0] - 1) if a1 < overlap[0] - 1 else None
    higher = (overlap[1] + 1, b1) if b1 > overlap[1] + 1 else None
    return [overlap, lower, higher]

def join_ranges(ranges):
    ranges.sort(key=lambda r: r[0])
    ix = 1
    while ix < len(ranges):
        (a1, b1), (a2, b2) = ranges[ix - 1], ranges[ix]
        if a1 <= b2 and a2 <= b1:
            ranges[ix - 1] = (min(a1, a2), max(b1, b2))
            ranges.pop(ix)
        else: ix += 1
    return ranges

for map in maps:
    tmp = []
    for dst, src, rng in map:
        diff = dst - src
        i = 0
        while i < len(ranges):
            overlap = split_by_overlap(ranges[i], (src, src + rng - 1))
            if overlap == None: i += 1
            else:
                ranges.pop(i)
                (a, b), lower, higher = overlap
                if lower != None: ranges.append(lower)
                if higher != None: ranges.append(higher)
                tmp.append((a + diff, b + diff))
    tmp.extend(ranges)
    ranges = join_ranges(tmp)
print(tmp[0][0])