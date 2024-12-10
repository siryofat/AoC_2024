class path_finder:
    def __init__(self, text_file: str):
        self.text_file = text_file
        self.array = []
        self.obstacle_positions = set()
        self.start_position = None
        self.start_direction = None
        self.array_size = None
        self.visited_positions = set()
        self.posible_loops = set()
        self.invalid_range = None

        self._read_text_file()
        self._get_array_size()
        self._get_invalid_range()

    def _read_text_file(self):
        with open(self.text_file, 'r') as file:
            for m, line in enumerate(file):
                stripped = line.strip()
                self.array.append(stripped)
                for n, char in enumerate(stripped):
                    if char == '#':
                        self.obstacle_positions.add((m,n))
                    elif char in '^>v<':
                        position = (m, n)
                        self.start_position = (position)
                        self.start_direction = char
                        self.visited_positions.add(position)

    def _get_array_size(self):
        m = len(self.array)
        n = len(self.array[0])
        self.array_size = (m, n)

    def _is_valid_position(self, current_position: tuple) -> bool:
        m, n = self.array_size
        i, j = current_position
        valid_x = 0 <= i < m
        valid_y = 0 <= j < n
        return valid_x and valid_y

    def _move_in_direction(self, position: tuple, direction: str) -> tuple:
        i, j = position
        moving_directions = {
            '^': (0,-1),
            '>': (1,0),
            'v': (0,1),
            '<': (-1,0),
        }
        moving_step = moving_directions[direction]
        col_step, line_step = moving_step
        next_position = (i+line_step, j+col_step)
        return next_position

    def _turn_right(self, direction:str) -> str:
        turn = {
            '^':'>',
            '>':'v',
            'v':'<',
            '<':'^'
        }
        return turn[direction]

    def _is_valid_boundary(self, position: tuple, direction: str, start: tuple) -> bool:
        i, j = start
        m, n = position
        if direction == '^':
            return i > m
        elif direction == 'v':
            return i < m
        elif direction == '>':
            return j < n
        elif direction == '<':
            return j > n

    def _is_possible_loop(self, start: tuple, direction: str, iteration:int = 1, fixed_start:tuple = None) -> bool:
        valid = True
        current_position = start
        start = fixed_start if fixed_start else start
        while valid:
            test_position = self._move_in_direction(current_position, direction)
            valid = self._is_valid_position(test_position)
            if valid:
                i, j = test_position
                test_char = self.array[i][j]
                if test_char == '#':
                    if iteration == 3:
                        valid_boundary = self._is_valid_boundary(current_position, direction, start)
                        return valid_boundary
                    next_direction = self._turn_right(direction)
                    iteration += 1
                    return self._is_possible_loop(current_position, next_direction, iteration, start)
                current_position = test_position
        return False


    def _step_aside(self, position: tuple, direction: str) -> tuple:
        direction = self._turn_right(direction)
        side_position = self._move_in_direction(position, direction)
        return side_position


    def _test_loop(self, position: tuple, direction: str, fixed_start: tuple = None) -> bool:
        fixed_start = fixed_start if fixed_start else position
        obs_pos = self._move_in_direction(position, direction)
        start_direction = (direction, self._turn_right(direction))
        direction = self._turn_right(direction)
        valid = True
        iteration = 0
        while valid:
            test_position = self._move_in_direction(position, direction)
            valid = self._is_valid_position(test_position) and iteration < 10000
            if valid:
                i, j = test_position
                char = self.array[i][j]
                if char == '#' or test_position == obs_pos:
                    direction = self._turn_right(direction)
                    iteration += 1
                elif test_position == fixed_start and direction in start_direction:
                    return True
                else:
                    position = test_position
        return False

    def populate_possible_loops(self, position: tuple, direction: str):
        is_loop = self._test_loop(position, direction)
        if is_loop:
            position = self._move_in_direction(position, direction)
            i, j = position
            if j == self.invalid_range[0][1]:
                top = self.invalid_range[1][0]
                bot = self.invalid_range[0][0]
                if top <= i <= bot:
                    return
            self.posible_loops.add(position)

    def _get_invalid_range(self):
        test_position = self._move_in_direction(self.start_position, self.start_direction)
        i, j = test_position
        test_char = self.array[i][j]
        while test_char != '#':
            test_position = self._move_in_direction(test_position, self.start_direction)
            i, j = test_position
            test_char = self.array[i][j]
        self.invalid_range = (self.start_position, (i, j))


    def populate_visited_positions(self):
        position = self.start_position
        direction = self.start_direction
        valid_position = True
        while valid_position:
            self.visited_positions.add(position)
            self.populate_possible_loops(position, direction)
            test_position = self._move_in_direction(position, direction)
            valid_position = self._is_valid_position(test_position)
            if valid_position:
                i, j = test_position
                test_char = self.array[i][j]
                if test_char == '#':
                    direction = self._turn_right(direction)
                else:
                    position = test_position


# Tester:
print("Tests:")
day06_test = path_finder('src/Day06-GuardGallivant/day06_test.txt')
day06_test.populate_visited_positions()
print(f'Visited positions: {len(day06_test.visited_positions)}')
print(f'Possible loops: {len(day06_test.posible_loops)}')

# Puzzle:
print("\nPuzzle:")
day06_part01 = path_finder('src/Day06-GuardGallivant/day06_input.txt')
day06_part01.populate_visited_positions()
print(f'Visited positions: {len(day06_part01.visited_positions)}')
print(f'Possible loops: {len(day06_part01.posible_loops)}')



#1575