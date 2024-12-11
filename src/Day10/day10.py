# declares a global because trying to go fast in solving the puzzles
data = []

def get_dirs_to_check(current_dir:str):
    reverser = {'t':'b', 'b':'t', 'l':'r', 'r':'l'}
    dir_reversed = reverser.get(current_dir, '')
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


def checker(start_point: tuple) -> int:
    global data
    max_rows = len(data)
    max_cols = len(data[0])

    visited = set()
    visits =[start_point]


    # get directions to check:
    dirs = 'tblr'
    while visits:
        # get starting value:
        current_pos = visits.pop()
        row, col = current_pos
        st_val = int(data[row][col])

        for current_dir in dirs:
            next_pos = move_in_direction(current_pos, current_dir)

            # check if visited to not check again.
            # if next_pos in visited:
            #     continue
            # else:
            #     visited.add(next_pos)

            # check if within bounds:
            nrow, ncol = next_pos
            if not(
                0 <= nrow < max_rows and 0 <= ncol < max_cols
            ): continue

            # check if value doesn't increase by one
            next_value = int(data[nrow][ncol])
            if next_value != st_val+1:
                continue

            # check if reached 9:
            if next_value == 9:
                visited.add(next_pos)
                continue

            visits.append(next_pos)

    return len(visited)


def iterate_data(data:list[list]):
    iterations = []
    for r, row in enumerate(data):
        for c, char in enumerate(row):
            if int(char) == 0:
                if (r,c) == (4,6):
                    print('')
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
    print(result)


main()