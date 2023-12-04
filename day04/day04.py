import re
input = open('input.txt').read().strip()
# import numpy as np

# part_one
def part_one():
    sum = 0 
    for line in input.split('\n'):
        cardval = 0
        line = line[line.find(':')+2:]
        crossed, winners = line.split('|')
        crossed = crossed[:][:-1]
        winners = winners[:][1:]
        # print('crossed =', '.'+crossed+'.')
        # print('winners =', '.'+winners+'.')
        wns = winners.split(' ')
        wns = [s.strip() for s in wns]
        for number in crossed.split(" "):
            number = number.strip()
            # print('number=', number)
            if number in wns and len(number)>0:
                # print('found(\''+number+'\'): ', (number in wns))
                if cardval == 0 :
                    cardval = 1
                else: 
                    cardval *= 2
            # print('cardvalue = ', cardval)
        sum += cardval
        # print()
    print(sum)
part_one()

# part two
def part_two():
    sum = 0 
    cards = 0
    copies = [1]*len(input.split('\n'))
    for ind, line in enumerate(input.split('\n')):
        cards += copies[0]
        cardval = 0
        line = line[line.find(':')+2:]
        crossed, winners = line.split('|')
        crossed = crossed[:][:-1]
        winners = winners[:][1:]
        wns = winners.split(' ')
        wns = [s.strip() for s in wns]
        for number in crossed.split(" "):
            number = number.strip()
            if number in wns and len(number)>0:
                cardval+=1
        for i in range(cardval):
            copies[ind+i+1] += copies[ind]
    for card in copies:
        sum += card
    print(sum)
part_two()