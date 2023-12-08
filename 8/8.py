import re
import numpy as np
from itertools import cycle
from math import lcm
f = open("input.txt").read().split('\n')
directions = f[0]
directions = re.sub('L', '0', directions)
directions = re.sub('R', '1', directions)
directions = np.array(list(directions), dtype = int)
directions_looped = cycle(directions)

nodes = {}
for line in f[2:]:
    nodes[re.search('[A-Z0-9]{3}\s=', line).group()[:3]] = (re.search('\([A-Z0-9]{3}', line).group()[1:], re.search('[A-Z0-9]{3}\)', line).group()[:3])


x = 'AAA'
for i, n in enumerate(directions_looped):
    x = nodes[x][n]
    if x == 'ZZZ':
        print('part 1: ', i+1)
        break

starting_points = []
for key in nodes.keys():
    if key[-1] == 'A':
        starting_points.append(key)


steps = []
for start in starting_points:
    x = start
    for i, n in enumerate(directions_looped):
        x = nodes[x][n]
        if x[-1] == 'Z':
            steps.append(i+1)
            break

print('part 2: ', lcm(*steps))




