lines = {}

requirements = {'red': 12, 'green': 13, 'blue': 14}

with open('day2/input2.txt') as file:
    for line in file:
        split = line.split(":")
        sets = split[1].split(";")
        sets = list(map(lambda x: x.split(","), sets))
        sets = list(map(lambda x: list(map(lambda y: y.strip(), x)), sets))

        lines[split[0]] = sets

def helper(l) -> list[int]:
    values = {'red': 0, 'green': 0, 'blue': 0}
    ret = []
    for game in l:
        for list in game:
            current = {'red': 0, 'green': 0, 'blue': 0}
            for item in list:
                valueAndColor = item.split(" ")
                v = int(valueAndColor[0])
                color = valueAndColor[1]
                current[color] += v
            values['red'] = max(values['red'], current['red'], 1)
            values['green'] = max(values['green'], current['green'], 1)
            values['blue'] = max(values['blue'], current['blue'], 1)
        add = values['red'] * values['green'] * values['blue']
        ret.append(add)
        values = {'red': 0, 'green': 0, 'blue': 0}
        
    return ret

ret = sum(helper(lines.values()))

print(ret)