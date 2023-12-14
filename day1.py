from operator import le, ge

with open("inputs/day1.txt") as f:
    inp = f.readlines()

# Part 1
s = 0
for line in inp:
    digits = [c for c in line if '0' <= c <= '9']
    s += int(digits[0] + digits[-1])
print(s)

# Part 2
nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
nums.extend(str(i) for i in range(1, 10))

def find_digit(s, cmp, init, fn):
    digit, ix = 0, init
    for i, n in enumerate(nums):
        t = fn(s, n)
        if t != -1 and cmp(t, ix):
            ix, digit = t, (i % 9) + 1
    return digit

s = 0
for line in inp:
    s += find_digit(line, le, len(line), str.find) * 10 + find_digit(line, ge, -1, str.rfind)
print(s)