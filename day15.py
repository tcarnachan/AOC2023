with open("inputs/day15.txt") as f:
    inp = f.read().split(',')

cache = {  }
def hash(s):
    if s not in cache:
        h = 0
        for c in s:
            h = ((h + ord(c)) * 17) % 256
        cache[s] = h
    return cache[s]

# Part 1
print(sum(hash(s) for s in inp))

# Part 2
boxes = [{} for _ in range(256)]
counter = 0
for s in inp:
    if s[-1] == '-':
        lbl = s[:-1]
        if lbl in boxes[hash(lbl)]:
            del boxes[hash(lbl)][lbl]
    else:
        lbl, n = s.split('=')
        box = boxes[hash(lbl)]
        if lbl in box:
            _, y = box[lbl]
            box[lbl] = (int(n), y)
        else:
            box[lbl] = (int(n), counter)
            counter += 1

s = 0
for ix, box in enumerate(boxes):
    lenses = sorted(box.values(), key=lambda x: x[1])
    for i, e in enumerate(lenses):
        s += (ix + 1) * (i + 1) * e[0]
print(s)