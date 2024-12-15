test = 'p=0,4 v=3,-3'

p, v = test.split()

def read_line_values(line_info:str) -> tuple:
    '''
    Gets line from input and cure it for processing:
    p=x,y v=vx,vy -> (x,y), (vx,vy)
    '''
    position, velocity = line_info.split()
    pos_x, pos_y = map(int, position.split('=')[1].split(','))
    vel_x, vel_y = map(int, velocity.split('=')[1].split(','))
    return (pos_x, pos_y), (vel_x, vel_y)

