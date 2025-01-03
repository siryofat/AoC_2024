import math
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

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
    cwd = Path(__file__).parent.resolve()
    print(cwd)
    file_path = cwd / 'day14.txt' #224554908
    quadrants = {'axis': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Q4': 0}
    min_factor = 999999999
    min_factor_index = 0

    data = []


    with open(file_path, 'r') as file:
        for line in file:
            data.append(line.strip())

    for i in range(seconds+1):
        plot_dict = {'x': [], 'y': [], 'quadrant': []}
        quadrants = {'axis': 0, 'Q1': 0, 'Q2': 0, 'Q3': 0, 'Q4': 0}
        for row in data:
            position, velocity = read_line_values(row)
            final_x, final_y = move_robot(position, velocity, i, space_dimensions)

            # Keep this to solve part 01:

            quadrant = get_quadrant(final_x, final_y, space_dimensions)
            quadrants[quadrant] += 1

            # This dict solves part 02:
            quadrant = get_quadrant(final_x, final_y, space_dimensions)
            plot_dict['x'].append(final_x)
            plot_dict['y'].append(final_y)
            plot_dict['quadrant'].append(quadrant)

        quadrants_values = [quadrants[quadrant] for quadrant in ('Q1', 'Q2', 'Q3', 'Q4')]
        safety_factor = math.prod(quadrants_values)
        if safety_factor < min_factor:
            min_factor = safety_factor
            min_factor_index = i
        # Plot the matrix to find the easter egg visualy:
        if i==min_factor_index: #6644
            print(f'{i=}')
            sns.scatterplot(x='x', y='y', data=plot_dict, hue='quadrant', palette=sns.color_palette('husl',5))
            plt.show()


    quadrants_values = [quadrants[quadrant] for quadrant in ('Q1', 'Q2', 'Q3', 'Q4')]
    safety_factor = math.prod(quadrants_values)

    print(quadrants)
    print(safety_factor)

    print(f'{min_factor=}')
    print(f'{min_factor_index=}')




main()