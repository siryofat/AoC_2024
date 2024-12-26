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

# creates a set to keep track of visited zones
visited_zones = set()
fence_prices = []

# populates data:
data = []
with open('src/Day12-GardenGroups/day12.txt', 'r') as file: #1396562
    for line in file:
        data.append(line.strip())

mrow = len(data)
mcol = len(data[0])

for r, row in enumerate(data):
    for c, item in enumerate(row):
        # if already in a zone, continue to next item:
        if (r,c) in visited_zones:
            continue

        # data structures to keep track of visited positions and queue
        visited = set()
        to_visit_queue = [(r, c)]
        fence_counter = 0
        dirs = 'tblr'

        while to_visit_queue:
            position = to_visit_queue.pop()

            # keeps track of visited positions:
            if position in visited:
                continue
            else:
                visited.add(position)

            for direction in dirs:
                test_pos = move_in_direction(position, direction)
                i, j = test_pos
                if not(0 <= i < mrow and 0 <= j < mcol):
                    fence_counter += 1
                    continue

                test_value = data[i][j]

                if test_value == item:
                    to_visit_queue.append(test_pos)
                else:
                    fence_counter += 1

        fence_perimeter = fence_counter
        zone_area = len(visited)
        fence_price = fence_perimeter * zone_area
        fence_prices.append(fence_price)

        # adds all visited spots to a visited_zones to not visit them again.
        visited_zones |= visited

total_cost = sum(fence_prices)

print(f'Total cost: {total_cost}')