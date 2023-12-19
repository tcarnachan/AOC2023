with open("inputs/day19.txt") as f:
    inp = f.read().split("\n\n")

workflows = {}
for flow in inp[0].splitlines():
    name, rules = flow[:-1].split('{')
    workflows[name] = rules.split(',')

def handle_rule(part, rule):
    if (ix := rule.find(':')) > -1:
        if (((op := rule.find('>')) > -1 and part[rule[:op]] > int(rule[op+1:ix]))
            or ((op := rule.find('<')) > -1 and part[rule[:op]] < int(rule[op+1:ix]))):
            return rule[ix+1:]
    else: return rule

def exec_wkflow(part, flow):
    for rule in flow:
        if res := handle_rule(part, rule):
            return exec_wkflow(part, workflows[res]) if res in workflows else res == 'A'

total = 0
for part_data in inp[1].splitlines():
    part = {}
    for rating in part_data[1:-1].split(','):
        name, val = rating.split('=')
        part[name] = int(val)
    if exec_wkflow(part, workflows['in']):
        total += sum(part.values())
print(total)