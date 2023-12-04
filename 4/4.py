f = open("input.txt").read().split('\n')
total = 0
cards = {}
n = 1
for line in f:
    values = line.split('|')
    card = values[0].split(' ')[2:]
    card = set([int(c) for c in card if c.isdigit()])
    winners = values[1].split(' ')
    winners = set([int(w) for w in winners if w.isdigit()])
    numbers = card.intersection(winners)
    cards[n] = {'card': card, 'winners':winners, 'numbers': len(numbers), 'copies': 1}
    score = 2 ** (len(numbers) - 1)
    if score >= 1:
        total += score
    n += 1

print('part 1: ', total)

for n in range(1, len(f)):
    numbers = cards[n]['numbers']
    if numbers > 0:
        for i in range(n+1, n+numbers+1):
            cards[i]['copies'] += 1 * cards[n]['copies']
    

total = 0
for n in range(1, len(f) + 1):
    total += cards[n]['copies']

print('part 2: ', total)