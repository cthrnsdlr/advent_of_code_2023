import numpy as np

f = open("test.txt").read().split('\n')
time = np.array(f[0].split()[1:], dtype=int)
distance = np.array(f[1].split()[1:], dtype = int)

winning = []
for i, t in enumerate(time):
    n = 0
    w = 0
    while n <= t:
        time_left = t - n
        dist = n * time_left
        if dist > int(distance[i]):
            w += 1
        n += 1
    winning.append(w)

print(np.prod(winning))