import sys

from collections import defaultdict

with open("inputs/day23.txt") as f:
    inp = f.read().splitlines()

# Move start/end inward, need to add 2 to distances later
start = (1, inp[0].index('.'))
end = (len(inp) - 2, inp[-1].index('.'))
inp[0] = inp[-1] = '#' * len(inp[0])

dists = defaultdict(dict)

def update_dists(dist, curr, prev, init):
    r, c = curr
    adj = [(r - 1, c)] if inp[r][c] == '^' else [(r, c + 1)] if inp[r][c] == '>' \
        else [(r + 1, c)] if inp[r][c] == 'v' else [(r, c - 1)] if inp[r][c] == '<' \
        else [(r1, c1) for r1, c1 in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)] if inp[r1][c1] != '#']
    adj = [a for a in adj if a != prev]
    if len(adj) == 1:
        if adj[0] == end: dists[init][end] = dist
        else: update_dists(dist + 1, adj[0], curr, init)
    elif len(adj) > 0:
        dists[init][curr] = dist
        for a in adj: update_dists(1, a, curr, curr)

lim = len(inp) * len(inp[0]) - sum([len([c for c in l if c == '#']) for l in inp])
sys.setrecursionlimit(lim)

update_dists(0, start, None, start)

visited = set()
def find_path(d, curr):
    if end in dists[curr].keys(): return d + dists[curr][end]
    res = -1
    for node, dist in dists[curr].items():
        if node not in visited:
            visited.add(node)
            res = max(res, find_path(d + dist, node))
            visited.remove(node)
    return res

visited.add(start)
print(find_path(1, start) + 2)

# Part 2
for k, v in dict(dists).items():
    for n, d in v.items():
        dists[n][k] = d
print(find_path(1, start) + 2)