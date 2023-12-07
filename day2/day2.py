lines = {}

requirements = {'red': 12, 'green': 13, 'blue': 14}

with open('day2/input2.txt') as file:
    for line in file:
        split = line.split(":")
        sets = split[1].split(";")
        sets = list(map(lambda x: x.split(","), sets))
        sets = list(map(lambda x: list(map(lambda y: y.strip(), x)), sets))

        lines[split[0]] = sets

def helper(l):
    values = {'red': 0, 'green': 0, 'blue': 0}
    for list in l:
        for item in list:
            valueAndColor = item.split(" ")
            v = int(valueAndColor[0])
            color = valueAndColor[1]
            values[color] += v
            if requirements['red'] < values['red'] or requirements['green'] < values['green'] or requirements['blue'] < values['blue']:
                return False
            values = {'red': 0, 'green': 0, 'blue': 0}
        
    return True

sum = 0
for game, cubes in lines.items():
    add = True
    if helper(cubes):
        sum += int(game.split(" ")[-1])

print(sum)