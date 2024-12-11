# declares a global because trying to go fast in solving the puzzles
data = []

def get_dirs_to_check(current_dir:str):
    reverser = {'t':'b', 'b':'t', 'l':'r', 'r':'l'}
    dir_reversed = reverser.get([current_dir], '')
    dirs = (current_dir for current_dir in 'tblr' if current_dir != dir_reversed)
    return dirs


def move_in_direction(start_index: tuple, direction: str) -> tuple:
    row, col = start_index
    moving_directions = {
        't': (-1,0),
        'r': (0,1),
        'b': (1,0),
        'l': (0,-1),
    }
    moving_step = moving_directions[direction]
    delta_row, delta_col = moving_step
    end_index = (row+delta_row, col+delta_col)
    return end_index


def checker(start_point: tuple, current_dir:str = '', counter:int = 0) -> int:
    global data
    max_rows = len(data)
    max_cols = len(data[0])

    visited = set()
    counter = counter if counter else 0

    # get starting value:
    row, col = start_point
    st_val = data[row][col]

    # get directions to check:
    dirs = get_dirs_to_check(current_dir)
    for current_dir in dirs:
        next_pos = move_in_direction(current_dir)

        # check if visited to not check again.
        if next_pos in visited:
            return

        # check if within bounds:
        if not(
            0 <= nrow < max_rows and 0 <= ncol < max_cols
        ): return

        # check if value doesn't increase by one
        nrow, ncol = next_pos
        next_value = data[nrow, ncol]
        if next_value != st_val+1:
            return

        # check if reached 9:
        if next_value == 9:
            counter += 1
            return

        checker(next_pos, current_dir, counter)

    return counter


def iterate_data(data:list[list]):
    iterations = []
    for r, row in enumerate(data):
        for c, char in enumerate(row):
            if char == 0:
                score = checker((r,c))
                iterations.append(score)
    return iterations


def main():
    global data

    with open('src/Day10/day10_test.txt', 'r') as file:
        for line in file:
            data.append(line.strip())

    result = iterate_data(data)

    print(sum(result))


main()