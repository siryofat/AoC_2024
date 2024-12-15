import math

def read_line_values(line_info:str) -> tuple:
    '''
    Gets line from input and cure it for processing:
    p=x,y v=vx,vy -> (x,y), (vx,vy)
    '''
    position, velocity = line_info.split()
    pos_x, pos_y = map(int, position.split('=')[1].split(','))
    vel_x, vel_y = map(int, velocity.split('=')[1].split(','))
    return (pos_x, pos_y), (vel_x, vel_y)

def move_robot(initial_position: tuple,
               velocity: tuple,
               time: int,
               space: tuple,) -> tuple:
    x, y = initial_position
    vx, vy = velocity
    x_max, y_max = space

    new_x = x + time * vx
    new_y = y + time * vy

    # Since it's goint to teleport, its enough to remove extra space
    # from final positions:
    extra_x = new_x // (x_max)
    extra_y = new_y // (y_max)
    corrected_x = new_x - extra_x * x_max
    corrected_y = new_y - extra_y * y_max

    return corrected_x, corrected_y


def get_quadrant(pos_x:int, pos_y:int, space:tuple) -> str:
    """
    Get x,y and dimension. Array is divided in four quadrants, ignoring
    items that fall in the middle axis.
    """
    max_x, max_y = space
    mid_y_axis = max_x // 2
    mid_x_axis = max_y // 2

    if 0 <= pos_x < mid_y_axis:
        if 0 <= pos_y < mid_x_axis:
            return 'Q1'
        elif pos_y > mid_x_axis:
            return 'Q3'
    elif pos_x > mid_y_axis:
        if 0 <= pos_y < mid_x_axis:
            return 'Q2'
        elif pos_y > mid_x_axis:
            return 'Q4'

    return 'axis'


def main():
    space_dimensions = (101,103)
    seconds=100
    file_path = 'src/Day14-RestroomRedoubt/day14.txt'
    quadrants = {'axis': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Q4': 0}

    with open(file_path, 'r') as file:
        for line in file:
            position, velocity = read_line_values(line.strip())
            final_x, final_y = move_robot(position, velocity, seconds, space_dimensions)

            quadrant = get_quadrant(final_x, final_y, space_dimensions)
            quadrants[quadrant] += 1

    quadrants_values = [quadrants[quadrant] for quadrant in ('Q1', 'Q2', 'Q3', 'Q4')]
    safety_factor = math.prod(quadrants_values)

    print(quadrants)
    print(safety_factor)


main()