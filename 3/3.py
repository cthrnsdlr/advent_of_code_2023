import re
import numpy as np

f = open("input.txt").read().split('\n')
positions = []
gears = []
for i, line in enumerate(f):
    numbers = re.finditer('\d+', line)
    stars = re.finditer('\*', line)
    for number in numbers:
        positions.append([[i, number.start(), number.end()], int(number.group())])
    
    for star in stars:
        gears.append([i, star.start()])

def neighbours(y,x):
    for i in [-1,0,1]:
        a = x+i
        if a<0 or a>=len(f[0]):
            continue
        for j in [-1,0,1]:
            b = y+j
            if b<0 or b>=len(f):
                continue
            if i == 0 and j == 0:
                continue
            yield f[b][a], [b, a]

parts = []
for number in positions:
    y = number[0][0]
    chars = []
    for x in range(number[0][1], number[0][2]):
        for n, coord in neighbours(y, x):
            chars.append(n)
    for c in chars:
        if re.findall('[^.^0-9]', c):
            parts.append(number[1])
            break
        

gear_ratios = []
for gear in gears:
    y = gear[0]
    x = gear[1]
    values = []
    for n, coord in neighbours(y,x):
        for number in positions:
            if (coord[0] == number[0][0]) & (coord[1] in range(number[0][1], number[0][2])):
                values.append(number[1])
                positions.remove(number)
    if len(values) == 2:
        gear_ratios.append(values[0] * values[1])

print('part 1: ' ,np.sum(parts))
print('part 2: ', np.sum(gear_ratios))
