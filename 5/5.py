import numpy as np
seeds, *mappings = open('test.txt').read().split('\n\n')
seeds = [int(seed) for seed in seeds.split(':')[1].split()]

def mapping(seeds, maps, n):
    print(seeds)
    m = maps[n]
    print(m)
    m = m.split('\n')
    name = m[1]
    m = m[1:]
    m = [[int(x) for x in line.split()] for line in m]

    for i, seed in enumerate(seeds):
        for map in m:
            if seed in range(map[0], map[0] + map[2],):
                seeds[i] = seed - (map[1] - map[0])
    
    print(seeds)

    if name == 'humidity-to-location map':
        return seeds
    else:
        return mapping(seeds, maps, n+1)

location = mapping(seeds, mappings, 0)
print(location)

