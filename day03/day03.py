import re
input = open('input.txt').read().strip()


# part_one
def part_one():
    lines = input.split('\n')
    sum = 0 
    for i, line in enumerate(lines):
        for m in re.finditer(r"\d+", line):
            print('numbers: ', line[m.start():m.end()])
            ispartnumber = False
            if m.start() == 0: 
                start = 0
            else: 
                start = m.start()-1
            if m.end() == len(line): 
                end = m.end() 
            else: 
                end = m.end()+1
            print('m.start, m.end, start, end', m.start(), m.end(), start, end)
            #check for line above:
            if i>0: 
                string = lines[i-1][start:end]
                print('current string: ', string)
                ispartnumber = bool(re.search(r"[^\d.]", string))
                print(ispartnumber)
            #check for the character before the string: 
            if m.start()>0:
                string = lines[i][m.start()-1]
                print('current string: ', string)
                ispartnumber = ispartnumber or bool(re.search(r"[^\d.]", string))
                print(ispartnumber)
            # Check for the character after the string: 
            if m.end() < len(line):
                string = lines[i][m.end()]
                print('current string: ', string)
                ispartnumber = ispartnumber or bool(re.search(r"[^\d.]", string))
                print(ispartnumber)
            # check for the line below:
            if i < len(lines)-1:
                string = lines[i+1][start:end]
                print('current string: ', string)
                ispartnumber = ispartnumber or bool(re.search(r"[^\d.]", string))
                print(ispartnumber)
            if ispartnumber:
                sum+= int(line[m.start():m.end()])
                print(line[m.start():m.end()])
            print(sum)
            print()

    print(sum)

part_one()

# part_two
"""
funktioniert noch nicht. Die intervalle müssen jeweils bis zum ende einer zahl erweitert werden und es muss separat geschaut werden, wie viele zahlen angrenzen. Idee ist, diese an nums zu appenden, auf die länge zu checken und bei len = 2 aufzuaddieren und am ende auszusummieren. 
"""

def part_two():
    lines = input.split('\n')
    sum = 0 
    for i, line in enumerate(lines):
        for m in re.finditer('\*', line):
            print('numbers: ', line[m.start():m.end()])
            isgear = False
            nums = []
            if m.start() == 0: 
                start = 0
            else: 
                start = m.start()-1
            if m.end() == len(line): 
                end = m.end() 
            else: 
                end = m.end()+1
            print('m.start, m.end, start, end', m.start(), m.end(), start, end)
            #check for line above:
            if i>0: 
                string = lines[i-1][start:end]
                print('current string: ', string)
                isgear = bool(re.search(r"[\d]", string))
                print(isgear)
            #check for the character before the string: 
            if m.start()>0:
                string = lines[i][m.start()-1]
                print('current string: ', string)
                isgear = isgear or bool(re.search(r"\d", string))
                print(isgear)
            # Check for the character after the string: 
            if m.end() < len(line):
                string = lines[i][m.end()]
                print('current string: ', string)
                isgear = isgear or bool(re.search(r"\d", string))
                print(isgear)
            # check for the line below:
            if i < len(lines)-1:
                string = lines[i+1][start:end]
                print('current string: ', string)
                isgear = isgear or bool(re.search(r"\d", string))
                print(isgear)
            if isgear:
                # sum += produkt
                print(line[m.start():m.end()])
            print(sum)
            print()

    print(sum)
