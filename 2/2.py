import re
import numpy as np
f = open("input.txt").read().split('\n')

possible = []
for i, game in enumerate(f):
    reds = list(map(lambda elem: int(elem.strip(' red')), re.findall('\d+\sred', game)))
    if any(r > 12 for r in reds):
        continue
    else:
        blues = list(map(lambda elem: int(elem.strip(' blue')), re.findall('\d+\sblue', game)))
        if any(b > 14 for b in blues):
            continue
        else:
            greens = list(map(lambda elem: int(elem.strip(' green')), re.findall('\d+\sgreen', game)))
            if any(g > 13 for g in greens):
                continue
            else:
                possible.append(i+1)

print(np.sum(possible))