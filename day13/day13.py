
def get_middle_points(number):
    return range(0, number - 1), number / 2
    
def print_patterns(pattern_1, pattern_2):
    for p1, p2 in zip(pattern_1, pattern_2):
        print(f'pattern 1: {p1}')
        print(f'pattern 2: {p2}')

def rotate_matrix(pattern):
    # Use zip with * to transpose the matrix
    return [list(row) for row in zip(*pattern)]
    
def check_if_symmetrical(pattern):
    middle_points, actual_middle = get_middle_points(len(pattern[0]))
    rounded_actual = int(actual_middle)
    for middle_point in middle_points:
        #print(f'left range: {list(range(middle_point, max(-1, (middle_point - rounded_actual) * 2), -1))[::-1]}')
        #print(f'right range: {list(range(middle_point + 1, min((middle_point + 1) * 2, int(actual_middle * 2))))}')
        left_side = []
        right_side = []
        for i in (range(middle_point, max(-1, (middle_point - rounded_actual) * 2), -1)):
            left_side.append(list(map(lambda x: x[i], pattern)))
        for i in (range(middle_point + 1, min((middle_point + 1) * 2, int(actual_middle * 2)))):
            right_side.append(list(map(lambda x: x[i], pattern)))
        if left_side == right_side:
            print("correct")
            #print_patterns(left_side, right_side)
            return middle_point + 1
    return 0

with open('day13/input13.txt') as file:
    input_str = file.read()

patterns = [x.split("\n") for x in input_str.strip().split("\n\n")]

return_sum = 0

for pattern in patterns:
    num = check_if_symmetrical(pattern)
    if (num == 0):
        print('trying horizontal')
        num_2 = check_if_symmetrical(rotate_matrix(pattern)) * 100
        if num_2 == 0:
            print('not found')
        else:
            return_sum += num_2
    else:
        return_sum += num

print(return_sum)