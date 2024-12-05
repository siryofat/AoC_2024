import numpy as np

def get_zone(array_size: tuple, current_index: tuple, limit: int) -> str:
    """
    Finds the zone of the index in the array:

    TL TT TR
    LL CC RR
    BL BB BR
    """

    m, n = array_size
    i, j = current_index

    # calculate zone bools:
    left_range = 0 <= j < limit-1
    right_range = m-limit < j <= m
    top_range = 0 <= i < limit-1
    bottom_range = n-limit < i <= n

    zone = ''
    if left_range:
        if top_range:
            zone = 'TL'
        elif bottom_range:
            zone = 'BL'
        else:
            zone = 'LL'
    elif right_range:
        if top_range:
            zone = 'TR'
        elif bottom_range:
            zone = 'BR'
        else:
            zone = 'RR'
    elif top_range:
        zone = 'TT'
    elif bottom_range:
        zone = 'BB'
    else:
        zone = 'CC'

    return zone

def get_directions_to_check(zone: str) -> list:
    directions = ['TT', 'TR', 'RR', 'BR', 'BB', 'BL', 'LL', 'TL']
    c1, c2 = zone
    directions_to_check = [direction for direction in directions if c1 not in direction and c2 not in direction]
    return directions_to_check

def move_in_direction(start_index: tuple, direction: str) -> tuple:
    i, j = start_index
    moving_directions = {
        'TT': (0,-1),
        'TR': (1,-1),
        'RR': (1,0),
        'BR': (1,1),
        'BB': (0,1),
        'BL': (-1,1),
        'LL': (-1,0),
        'TL': (-1,-1)
    }
    moving_step = moving_directions[direction]
    x, y = moving_step
    end_index = (i+y, j+x)
    return end_index

def get_array_size(txt_array: list) -> tuple:
    m = len(txt_array)
    n = len(txt_array[0])-1
    return (m, n)

def is_valid_word_length(word_to_check: str) -> int:
    word_length = len(word_to_check)

    if word_length % 2 == 0:
        raise ValueError(f'A valid diagonal size must be an odd number, got {word_length} instead.')

    mid_side = (word_length - 1) / 2
    return mid_side

def is_in_valid_cross_zone(array_size: tuple, current_index: tuple, mid_side: int) -> bool:
    """
    Validates index to get a cross without going out of index.
    \./.....\./
    .XXXXXXXXX.
    /X\...../.\
    """

    m, n = array_size
    i, j = current_index

    # checks for out of bounds bools:
    invalid_top = 0 <= j < mid_side
    invalid_bottom = m - mid_side <= j < n
    invalid_left = 0 <= i < mid_side
    invalid_rigth = m - mid_side <= i < m

    return not any([invalid_bottom, invalid_left, invalid_rigth, invalid_top])

def get_diagonal_word(current_index: tuple, cross_leg_size: int, directions: str) -> str:
    word = ''
    for direction in directions.split('-'):
        pass

def get_crossed_word(current_index: tuple, cross_leg_size: int) -> tuple:
    pass

# the solvers:
def part_one():
    # read txt file:
    with open('src/Day04-CeresSearch/day04_input.txt', 'r') as file:
        lines = file.readlines()

    array_size = get_array_size(lines)
    word_to_find = 'XMAS'
    start_letter = 'A'
    limit = 1
    total_score = 0
    tests = ['MAS', 'SAM']

    for m, line in enumerate(lines):
        for n, letter in enumerate(line):
            if letter == start_letter:
                index = (m, n)
                test_index = index
                if is_in_valid_cross_zone(array_size, index, limit):
                    first_word = lines[m-1][n-1] + 'A' + lines[m+1][n+1]
                    second_word = lines[m-1][n+1] + 'A' + lines[m+1][n-1]
                    if first_word in tests and second_word in tests:
                        total_score += 1

    print(total_score)


def part_two():
    # Future me, I'm so sorry.
    # read txt file:
    with open('src/Day04-CeresSearch/day04_input.txt', 'r') as file:
        lines = file.readlines()

    array_size = get_array_size(lines)
    word_to_find = 'MAS'
    mid_letter = word_to_find[1]
    limit = 2
    total_score = 0

    for m, line in enumerate(lines):
        for n, letter in enumerate(line):
            if letter == mid_letter:
                index = (m, n)
                test_index = index
                zone = get_zone(array_size, index, limit)
                directions_to_check = get_directions_to_check(zone)
                check_score = 0
                for direction in directions_to_check:
                    for character in word_to_find:
                        i, j = test_index
                        test_char = lines[i][j]
                        if test_char == character:
                            check_score += 1
                        temp_index = move_in_direction(test_index, direction)
                        test_index = temp_index
                    if check_score == limit:
                        total_score += 1
                    check_score = 0
                    test_index = index

    print(total_score)

part_one()