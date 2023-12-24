from collections import defaultdict
import heapq

with open("inputs/day17.txt") as f:
    inp = [list(map(int, l)) for l in f.read().splitlines()]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ROWS, COLS = len(inp), len(inp[0])

def add(a, b): return (a[0] + b[0], a[1] + b[1])

def get_neighbours(node, min_blocks, max_blocks):
    pos, dir = node
    neighbours = []
    for delta in [1, 3]:
        d = (dir + delta) % 4
        tmp, dist = pos, 0
        for i in range(max_blocks):
            tmp = add(tmp, dirs[d])
            if 0 <= tmp[0] < ROWS and 0 <= tmp[1] < COLS:
                dist += inp[tmp[0]][tmp[1]]
                if i >= min_blocks - 1:
                    neighbours.append(((tmp, d), dist))
            else: break
    return neighbours

infty = ROWS * COLS * 9
end = (ROWS - 1, COLS - 1)

def init_dists(min_blocks, max_blocks):
    dists = defaultdict(lambda: infty)
    dists[((0, 0), 1)] = 0
    dist = 0
    for i in range(1, max_blocks + 1):
        dist += inp[0][i]
        if i >= min_blocks:
            dists[((0, i), 1)] = dist
    return dists

class SortedList:
    def __init__(self):
        self.rev_lookup = {}
        self.keys = []
        self.lookup = defaultdict(set)
        self.count = 0
    
    def not_empty(self):
        return self.count > 0
    
    def get(self):
        ix = heapq.heappop(self.keys)
        item = self.lookup[ix].pop()
        del self.rev_lookup[item]
        self.count -= 1
        return item
    
    def add(self, item, priority):
        if item in self.rev_lookup:
            # Probably a better way of handling this
            p = self.rev_lookup[item]
            if p == priority: return
            self.lookup[p].remove(item)
            self.keys.remove(p)
            heapq.heapify(self.keys)
        self.rev_lookup[item] = priority
        self.lookup[priority].add(item)
        heapq.heappush(self.keys, priority)
        self.count += 1

def dijkstra(dists, get_neighbours):
    visited = set()
    to_visit = SortedList()
    for k, v in dists.items(): to_visit.add(k, v)
    while to_visit.not_empty():
        curr = to_visit.get()
        if curr[0] == end: return dists[curr]
        visited.add(curr)

        for adj, dist in get_neighbours(curr):
            if adj not in visited:
                dists[adj] = min(dists[adj], dists[curr] + dist)
                to_visit.add(adj, dists[adj])

# Part 1
print(dijkstra(init_dists(0, 3), lambda n: get_neighbours(n, 0, 3)))

# Part 2
print(dijkstra(init_dists(4, 10), lambda n: get_neighbours(n, 4, 10)))