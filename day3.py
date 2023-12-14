import re

with open("inputs/day3.txt") as f:
    inp = f.read()

# Part 1
s = 0
nums = re.finditer("(\d+)", inp.replace("\n", ""))
inp = inp.splitlines()
width, height = len(inp[0]), len(inp)
part_nums = [] # [(row, (start, end), num)]
for n in nums:
    row, start = divmod(n.start(), width)
    end = (n.end() - 1) % width
    
    adjacent = ""
    if row > 0: adjacent += inp[row - 1][max(start - 1, 0):min(end + 1, width - 1) + 1]
    if row < height - 1: adjacent += inp[row + 1][max(start - 1, 0):min(end + 1, width - 1) + 1]
    if start > 0: adjacent += inp[row][start - 1]
    if end < width - 1: adjacent += inp[row][end + 1]
    
    if re.search("[^\d\.]", adjacent):
        part_nums.append((row, (start, end), int(inp[row][start:end + 1])))
print(sum(n for (_, _, n) in part_nums))

# Part 2
s = 0
stars = re.finditer("(\*)", "".join(inp))
for star in stars:
    r, c = divmod(star.start(), width)
    adj = [n for (nr, (s, e), n) in part_nums
           if abs(nr - r) < 2 and (s - 1) <= c <= (e + 1)]
    if len(adj) == 2:
        s += adj[0] * adj[1]
print(s)
