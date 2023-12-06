import re
import numpy as np
f = open("input.txt").read().split('\n')

powers = []
for i, game in enumerate(f):
    reds = list(map(lambda elem: int(elem.strip(' red')), re.findall('\d+\sred', game)))
    blues = list(map(lambda elem: int(elem.strip(' blue')), re.findall('\d+\sblue', game)))
    greens = list(map(lambda elem: int(elem.strip(' green')), re.findall('\d+\sgreen', game)))

    power = max(reds) * max(blues) * max(greens)

    powers.append(power)


print(np.sum(powers))