import re
input = open('input.txt').read().strip()
import numpy as np

# part_one
def part_one():
    sum = 0 
    for line in input.split('\n'):
        digits = []
        for c in line:
            if c.isdigit():
                digits.append(c)
        sum += int(digits[0]+digits[-1])
    print(sum)

part_one()

# part two:
digit_names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def find_number_indices(_string, digit):
    locations_words = []
    if digit_names[digit] in _string:
        for m in re.finditer(digit_names[digit], _string):
            locations_words.append(m.start()) 
        return locations_words

def part_two():
    sum = 0 
    for line in input.split('\n'):
        # print(line)
        number_places = [[],[],[],[],[],[],[],[],[],[]]
        for val, name in enumerate(digit_names):
            for m in re.finditer(name, line):
                if name in line:
                    number_places[val].append(m.start())
            for m in re.finditer(str(val), line):
                if str(val) in line:
                    number_places[val].append(m.start())
        first, last = None, None
        for val, name in enumerate(digit_names):
            if number_places[val] != []:
                return

        # for n in range(len(digit_names)):
        #     number_places.append(find_number_indices(line, n))
        # print('number_places = ', number_places)
        # print('minimum_entry = ', min(number_places))
        # print('minimum_entry_index = ', number_places.index(min(number_places)))
        # print('maximum_entry = ', max(number_places))
        # print('maximum_entry_index = ', number_places.index(max(number_places)), '\n')
    
    print(sum)

part_two()

def part_two_youtube():
    sum = 0
    for line in input.split('\n'):
        digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            for val, name in enumerate(digit_names):
                if line[i:].startswith(name):
                    digits.append(str(val))
        sum += int(digits[0]+digits[-1])
    print(sum)

part_two_youtube()

# test = '13onetwonethree45fouroneleven'
# print([m.start() for m in re.finditer('one', test)])
# for m in re.finditer('one', test):
#     print(test[m.start():m.start()+len('one')])
