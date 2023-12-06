seeds, *mappings = open('input.txt').read().split('\n\n')
seeds = [int(seed) for seed in seeds.split(':')[1].split()]

def mapping(seeds, map):
    m = map.split('\n')[1:]
    m = [[int(x) for x in line.split()] for line in m]
    for i, seed in enumerate(seeds):
        for map in m:
            if seed in range(map[1], map[1] + map[2]):
                seeds[i] = seed - (map[1] - map[0])
    

for i, map in enumerate(mappings):
    mapping(seeds, map)
    print(i)

print(min(seeds))

