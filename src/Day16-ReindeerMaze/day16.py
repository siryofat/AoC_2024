from pathlib import Path
from collections import deque
from itertools import pairwise

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


maze = []
file_path = Path(__file__).parent / 'day16_test.txt'

with open(file_path, 'r') as file:
    for r, line in enumerate(file):
        maze.append(line.strip())
        if 'E' in line:
            exit_pos = (r,line.find('E'))
        if 'S' in line:
            start_pos = (r, line.find('S'))


for line in maze:
    print(line)

debug_maze = [['..' for _ in range(len(maze[0]))] for _ in range(len(maze))]


queue = deque()
queue.append(start_pos)
visited = set()
visited.add(start_pos)
found = False
solve_path = deque()
solve_path.append('r')
possible_paths = []

i=0

while queue:
    position = queue.popleft()
    test_path = solve_path.popleft()
    visited.add(position)

    for direction in 'trbl':
        test_position = move_in_direction(position, direction)
        r, c = test_position
        if not(0 <= r < len(maze) and 0 <= c < len(maze[0])):
            continue

        test_value = maze[r][c]
        if test_value == '#' or test_position in visited:
            continue

        if test_position == exit_pos:
                found = True
                possible_paths.append(test_path + direction)
                continue

        queue.append(test_position)
        solve_path.append(test_path + direction)
        debug_maze[r][c] = f'{i:02d}'
        i+=1

print(f'{exit_pos=}, {start_pos=}')

possible_scores = []

#short_path = 'rttttttttttrrbbbbbbbbbbrrttrrrrrrttrrttrrtttttttt'
#short_path = 'rttrrrrttttrrrrrrbbbbbbrrtttttttttttt'
for short_path in possible_paths:
    turns = 0
    for char, next_char in pairwise(short_path):
        if char != next_char:
            turns += 1

    score = len(short_path) + (turns*1000) - 1
    print(f'{score=}')
    possible_scores.append(score)

# for line in maze:
#     print(line)

solved_maze = []
for line in maze:
    solved_maze.append([c for c in line])

# for line in solved_maze:
#     print(line)

move_dir = {
    't': '^',
    'r': '>',
    'b': 'v',
    'l': '<'
}

solved_position = start_pos
for ca in possible_paths[1][1:]:
    r, c = solved_position
    solved_maze[r][c] = move_dir[ca]
    solved_position = move_in_direction(solved_position, ca)

for row in solved_maze:
    print(''.join(row))

print(min(possible_scores))