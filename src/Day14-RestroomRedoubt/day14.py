test = 'p=2,4 v=2,-3'

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

p, v = read_line_values(test)
x, y = move_robot(p,v,5,(11,7))
