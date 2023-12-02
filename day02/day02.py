input = open('input.txt').read().strip()

# part_one
def part_one():
    # cubes = 12 red cubes, 13 green cubes, and 14 blue cubes
    red, green, blue = 12, 13, 14
    colors = 'red', 'green', 'blue'
    sum = 0 
    for line in input.split('\n'):
        # print(line)
        id = int(line[5:line.find(':')]) 
        val = True
        for hand in line[line.find(': ')+1:].split(';'): 
            # print('Hand: ', hand)
            for cubes in hand.split(','):
                for number, name in zip((red, green, blue), colors): 
                    if name in cubes:
                        # print(str(number)+name, int(cubes[:cubes.find(' '+name)]))
                        if int(cubes[:cubes.find(' '+name)]) > number:
                            val = False
        # print('Möglich: ', val, '\n')
        if val:
            sum += id    
    print(sum)
part_one()

# part two
def part_two():
    # cubes = 12 red cubes, 13 green cubes, and 14 blue cubes
    colors = 'red', 'green', 'blue'
    red, green, blue = 12, 13, 14
    sum = 0 
    for line in input.split('\n'):
        mincolor = [0, 0, 0]
        id = int(line[5:line.find(':')]) 
        val = True
        for hand in line[line.find(': ')+1:].split(';'): 
            for cubes in hand.split(','):
                for ind, name in enumerate(colors): 
                    if name in cubes:
                        amount = int(cubes[:cubes.find(' '+name)]) 
                        if amount > mincolor[ind]:
                            mincolor[ind] = amount
        sum += mincolor[0]*mincolor[1]*mincolor[2]
    print(sum)
part_two()