import re
input = open('input.txt').read().strip()
# input = open('s.txt').read().strip()
# import numpy as np

# part_one
def part_one():
    sum = 1
    lines = input.split('\n')
    times = lines[0][lines[0].find(': ')+1:].strip().split(' ')
    # times = times[times.isdigit()]
    distances = lines[1][lines[1].find(': ')+1:].strip().split(' ')
    times.remove('')
    T = []
    for i, t in enumerate(times):
        if times[i] != '':
            T.append(int(times[i]))
    D = []
    for i, t in enumerate(distances):
        if distances[i] != '':
            D.append(int(distances[i]))
    for t, d in zip(T, D):
        mogl = 0
        for s in range(t):
            if (t-s)*s > d: 
                mogl += 1
        sum *= mogl
    print(sum)

part_one()

# part_two
def part_two():
    sum = 1
    lines = input.split('\n')
    times = lines[0][lines[0].find(': ')+1:].strip().split(' ')
    # times = times[times.isdigit()]
    distances = lines[1][lines[1].find(': ')+1:].strip().split(' ')
    times.remove('')
    T = []
    Te = ''
    for i, t in enumerate(times):
        if times[i] != '':
            T.append(times[i])
    for i in T: 
        Te += i
    T = int(Te)
    D = []
    De = ''
    for i, t in enumerate(distances):
        if distances[i] != '':
            D.append(distances[i])
    for i in D: 
        De += i
    D = int(De)
    mogl = 0
    for s in range(T):
        if (T-s)*s > D: 
            mogl += 1
    sum = mogl
    print(sum)

part_two()
