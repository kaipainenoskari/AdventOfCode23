summa = 0

with open('day4/input4.txt') as file:
    x = sum(1 for line in file)
with open('day4/input4.txt') as file:
    my_dict = {i: 1 for i in range(1, x + 1)}
    for line in file:
        line = line.rstrip().replace('  ', ' ')
        split = line.split('|')
        win_string, own_string = split[0].rstrip(), split[1].lstrip()
        win_string_split = win_string.split(':')
        card_number = int(win_string_split[0].split(' ')[-1])
        win_list = list(map(lambda x: int(x), win_string_split[1].lstrip().split(' ')))
        own_list = list(map(lambda x: int(x), own_string.split(' ')))
        points = 0
        for win in own_list:
            if win in win_list:
                points += 1
        for i in range(card_number + 1, card_number + points + 1):
            my_dict[i] += 1 * my_dict[card_number]
        summa += points

print(sum(my_dict.values()))