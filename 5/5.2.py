seeds, *mappings = open('test.txt').read().split('\n\n')
seeds = [int(t) for t in seeds.split(':')[1].split()]

seeds_total = []
for s in [*zip(seeds[0::2], seeds[1::2])]:
    [seeds_total.append(i) for i in range(s[0], s[0] + s[1])]

seeds_total = set(seeds_total)
unmapped = [0]
location = [0]


def mapping(location, map):
    m = map.split('\n')[1:]
    m = [[int(x) for x in line.split()] for line in m]
    for i, seed in enumerate(location):
        for map in m:
            if seed in range(map[0], map[0] + map[2]):
                location[i] = seed - (map[0] - map[1])
    return location
    

while True:
    for i, map in enumerate(reversed(mappings)):
        mapping(location, map)
    if location[0] in seeds_total:
        print(unmapped, location[0])
        break
    unmapped[0] += 1
    location[0] = unmapped[0]

