from functools import cmp_to_key, partial
from collections import Counter

with open("inputs/day7.txt") as f:
    inp = [l.split() for l in f.readlines()]

# Part 1
cards = "AKQJT98765432"

def type(hand):
    count = [c for _, c in Counter(hand).most_common(2)]
    # High card
    if count[0] == 1: return 1
    # Pair or Two pair
    if count[0] == 2: return count[1] + 1
    # Three of a kind or Full house
    if count[0] == 3: return count[1] + 3
    # Four of a kind or Five of a kind
    return count[0] + 2

def cmp(a, b, type_fn=type):
    hand1, hand2 = a[0], b[0]
    t1, t2 = type_fn(hand1), type_fn(hand2)
    if t1 == t2:
        for c1, c2 in zip(hand1, hand2):
            if c1 != c2:
                return cards.index(c2) - cards.index(c1)
    return t1 - t2

inp.sort(key=cmp_to_key(cmp))
print(sum((i + 1) * int(bid) for i, (_, bid) in enumerate(inp)))

# Part 2
cards = "AKQT98765432J"
def get_type(hand):
    return max(type(hand.replace("J", c)) for c in cards)
inp.sort(key=cmp_to_key(partial(cmp, type_fn=get_type)))
print(sum((i + 1) * int(bid) for i, (_, bid) in enumerate(inp)))