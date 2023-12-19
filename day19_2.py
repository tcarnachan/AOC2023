with open("inputs/day19.txt") as f:
    inp = f.read().split("\n\n")

workflows = { 'A': ['A'], 'R': ['R'] }
for flow in inp[0].splitlines():
    name, rules = flow[:-1].split('{')
    tmp = []
    for rule in rules.split(','):
        if (ix := rule.find(':')) > -1:
            op = max(rule.find('<'), rule.find('>'))
            tmp.append(('xmas'.index(rule[:op]), rule[op], int(rule[op+1:ix]), rule[ix+1:]))
        else: tmp.append(rule)
    workflows[name] = tmp

def get_valid(name, valid):
    total = 0
    for rule in workflows[name]:
        if rule == 'A':
            t = 1
            for s, e in valid: t *= e - s + 1
            total += t
        elif rule == 'R': continue
        elif rule in workflows: total += get_valid(rule, list(valid))
        else:
            attr, op, val, target = rule
            lower, upper = valid[attr]
            if op == '<':
                if val <= lower: continue
                tmp = min(upper, val - 1)
                valid[attr] = (lower, tmp)
                total += get_valid(target, list(valid))
                valid[attr] = (val, upper)
            else:
                if val >= upper: continue
                tmp = max(lower, val + 1)
                valid[attr] = (tmp, upper)
                total += get_valid(target, list(valid))
                valid[attr] = (lower, val)
    return total
        
print(get_valid('in', [(1, 4000), (1, 4000), (1, 4000), (1, 4000)]))