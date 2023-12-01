import re
import numpy as np

f = open("input.txt").read().split('\n')

values = []
for line in f:
    numbers = []
    for char in line:
        if char.isdigit():
            numbers.append(char)
    values.append(int(numbers[0] + numbers[-1]))

print('part 1: ', np.sum(values))

words_to_numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

values = []
for line in f:
    num = None
    i = len(line)
    while i > 0:
        num = re.findall('one|two|three|four|five|six|seven|eight|nine|[0-9]',line[i-5:i])
        if num:
            num = num[-1]
            if num.isdigit():
                end = num
            else:
                end = words_to_numbers[num]
            break
        else: 
            i -=1
    start = re.search('one|two|three|four|five|six|seven|eight|nine|[0-9]',line).group()
    if start.isalpha():
        start = words_to_numbers[start]
    values.append(int(start + end))

print('part 2: ', np.sum(values))