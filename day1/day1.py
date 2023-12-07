import re

def check3(s):
    w = s[0:3]
    if w == 'one':
        return '1'
    elif w == 'two':
        return '2'
    elif w == 'six':
        return '6'
    else: return ''

def check4(s):
    w = s[0:4]
    if w == 'four':
        return '4'
    elif w == 'five':
        return '5'
    elif w == 'nine':
        return '9'
    else: return ''

def check5(s):
    w = s[0:5]
    if w == 'three':
        return '3'
    elif w == 'seven':
        return '7'
    elif w == 'eight':
        return '8'
    else: return ''

def helper(l):
    i = 0
    copy = l
    s = ''
    while i < len(l):
        if copy[0].isdigit():
            s += copy[0]
        elif i <= len(l) - 3:
            s += check3(copy)
            if i <= len(l) - 4:
                s += check4(copy)
                if i <= len(l) - 5:
                    s += check5(copy)
        copy = copy[1:]
        i += 1
    return s
    

lines = list[str]()
sum = 0

with open('day1/input1.txt') as file:
    lines = [line.rstrip() for line in file]

for l in lines:
    l = l.strip()
    l = helper(l)
    numbers = re.findall(r'\d+', l)
    numbersStr = ''.join([str(elem) for elem in numbers])
    num = int(numbersStr[0]) * 10 + int(numbersStr[-1])
    sum += num

print(sum)