from collections import OrderedDict

i = 0
j = 0
numbers = []
rowLength = 0
columnLength = 0

def inBound(x, y):
    return x >= 0 and x < rowLength and y >= 0 and y < columnLength

def checkAllSides(pos):
    x = pos[0]
    y = pos[1]
    for j in range(-1, 2):
        for i in range(-1, 2):
            curX = x + i
            curY = y + j
            if (inBound(curX, curY)):
                current = input[curY][curX]
                if (not current.isnumeric() and current != '.'):
                    return True
    return False



with open('day3/input3.txt') as file:
    input = [line.rstrip() for line in file]
    for line in input:
        if rowLength == 0:
            rowLength = len(line)
        addedList = []
        for char in line:
            if (char.isnumeric()):
                addedList.append((int(char), (i, j)))
            elif (len(addedList) > 0):
                numbers.append(addedList)
                addedList = []
            else:
                addedList = []
            i += 1
        if (len(addedList) > 0):
            numbers.append(addedList)
        i = 0
        j += 1
    columnLength = j

#print(numbers)

numbersToSum = []

for longNumber in numbers:
    for number, pos in longNumber:
        #print(number, pos)
        if (checkAllSides(pos)):
            numbersToSum.append(longNumber)
            break

numbersToSum = list(map(lambda x: list(map(lambda y: y[0], x)), numbersToSum))

print(numbersToSum)

sum = 0
for numberList in numbersToSum:
    x = 1
    numberList.reverse()
    add = 0
    for number in numberList:
        add += number * x
        x *= 10
    print(add)
    sum += add

print(sum)

# List of dicts number -> coordinate
# def inBound(pos: coordinate) -> boolean checks if the pos is inbound 
# def check(pos: coordinate) -> boolean checks if there are symbols around the pos