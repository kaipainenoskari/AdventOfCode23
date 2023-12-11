from collections import Counter, defaultdict

def in_bound(x, y):
    return 0 <= x < row_length and 0 <= y < column_length

def check_all_sides(pos):
    x, y = pos
    for j in range(-1, 2):
        for i in range(-1, 2):
            cur_x, cur_y = x + i, y + j
            if in_bound(cur_x, cur_y):
                current = grid[cur_y][cur_x]
                if current == '*':
                    return (cur_x, cur_y)
    return (-1, -1)

with open('day3/input3.txt') as file:
    grid = [line.rstrip() for line in file]

numbers = []
row_length, column_length = len(grid[0]), len(grid)

for j, line in enumerate(grid):
    added_list = []
    for i, char in enumerate(line):
        if char.isnumeric():
            added_list.append((char, (i, j)))
        elif len(added_list) > 0:
            numbers.append(added_list)
            added_list = []
    if len(added_list) > 0:
        numbers.append(added_list)

numbers_to_sum = []

for long_number in numbers:
    for number, pos in long_number:
        current = check_all_sides(pos)
        if current != (-1, -1):
            numbers_to_sum.append((long_number, current))
            break

numbers_to_sum = [(int(''.join(map(lambda y: y[0], x[0]))), x[1]) for x in numbers_to_sum]

# Count occurrences of second values
second_value_counts = Counter(item[1] for item in numbers_to_sum)

# Filter tuples where the second value appears at least 2 times
filtered_list = [item for item in numbers_to_sum if second_value_counts[item[1]] >= 2]

# Use a defaultdict to store products for each unique second value
product_dict = defaultdict(lambda: 1)

# Calculate products for each unique second value
for item in filtered_list:
    product_dict[item[1]] *= item[0]  # Accumulate the product

products = sum(product_dict.values())

print(products)
