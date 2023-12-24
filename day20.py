from math import lcm

with open("inputs/day20.txt") as f:
    inp = f.read().splitlines()

LOW, HIGH = 0, 1

class FlipFlop:
    OFF = LOW
    ON = HIGH

    def __init__(self):
        self.status = FlipFlop.OFF
    
    def pulse(self, _, pulse):
        if pulse == LOW:
            self.status = 1 - self.status
            return self.status

class Conjunction:
    def __init__(self, inps):
        self.mem = dict([(name, LOW) for name in inps])
    
    def pulse(self, inp, pulse):
        self.mem[inp] = pulse
        if all(v == HIGH for v in self.mem.values()):
            return LOW
        return HIGH

class Broadcaster:
    def pulse(self, _, pulse):
        return pulse

dests = {}
for line in inp:
    src, targets = line.replace(' ', "").split('->')
    if src != 'broadcaster': src = src[1:]
    dests[src] = targets.split(',')
modules = {}
for line in inp:
    mod = line.split(' ->')[0]
    if mod == 'broadcaster':
        modules[mod] = Broadcaster()
    elif mod[0] == '%':
        modules[mod[1:]] = FlipFlop()
    else:
        inps = [k for k, v in dests.items() if mod[1:] in v]
        modules[mod[1:]] = Conjunction(inps)

low, high = 0, 0
for _ in range(1000):
    queue = [('broadcaster', None, LOW)]
    while len(queue) > 0:
        src, inp, pulse = queue.pop(0)
        if pulse == LOW: low += 1
        else: high += 1
        if src in modules and (ret := modules[src].pulse(inp, pulse)) != None:
            for dst in dests[src]:
                queue.append((dst, src, ret))
print(low * high)

"""
rx <- &zh
          <- &xc
                  <- &ps
          <- &th
                  <- &kh
          <- &pd
                  <- &mk
          <- &bp
                  <- &ml
zh needs to remember high pulse from all [xc, th, pd, bp]
each of [xc, th, pd, bp] need to remember low pulse from each of [ps, kh, mk, ml] respectively
"""

targets = ['ps', 'kh', 'mk', 'ml']
counters = [0, 0, 0, 0]

for k, v in modules.items():
    if type(v) == type(FlipFlop()):
        modules[k] = FlipFlop()
    elif type(v) == type(Conjunction):
        modules[k] = Conjunction(v.mem.keys())

for count in range(1000000):
    queue = [('broadcaster', None, LOW)]
    while len(queue) > 0:
        src, inp, pulse = queue.pop(0)
        if src in modules and (ret := modules[src].pulse(inp, pulse)) != None:
            for dst in dests[src]:
                if src in targets and ret == LOW:
                    counters[targets.index(src)] = count + 1
                queue.append((dst, src, ret))
    if all(c != 0 for c in counters):
        break

print(lcm(*counters))