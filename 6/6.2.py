import numpy as np

f = open("input.txt").read().split('\n')
time = f[0].split()[1:]
time = int(''.join(time))
distance = f[1].split()[1:]
distance = int(''.join(distance))

w = 0
n = 0
while n <= time:
    time_left = time - n
    dist = n * time_left
    if dist > distance:
        w += 1
    elif (w > 0) & (dist < distance):
        break
    n += 1

print(w)