with open("inputs/day4.txt") as f:
    inp = f.readlines()

# Part 1
matches = []
s = 0
for line in inp:
    card = line.split(": ")[1].split(" | ")
    winning = card[0].split()
    matches.append(len([n for n in card[1].split() if n in winning]))
    if matches[-1] > 0: s += 2 ** (matches[-1] - 1)
print(s)

# Part 2
lookup = [[0 for _ in range(len(inp))] for _ in range(len(inp))]
# Starting from the last card
for i in range(len(inp) - 1, -1, -1):
    # Win copies of following cards
    for j in range(i + 1, min(i + matches[i] + 1, len(inp))):
        lookup[i][j] += 1
        # Add the copies the copy wins
        for k in range(len(inp)):
            lookup[i][k] += lookup[j][k]
print(sum(sum(l) for l in lookup) + len(inp))