def add_tuples(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])

def pawn(pos, color):
    colors = {'B': (0, -2), 'W': (0, 2)}
    return add_tuples(pos, colors[color])
    
def king(pos, direction):
    directions = {'N': (0, 1), 'NE': (1, 1), 'NW': (-1, 1), 'E': (1, 0), 'SE': (1, -1), 'S': (0, -1), 'W': (-1, 0), 'SW': (-1, -1)}
    return add_tuples(pos, directions[direction])

def castle(pos, direction, distance):
    directions = {'N': (0, distance), 'S': (0, -1 * distance), 'E': (distance , 0), 'W': (-1 * distance, 0)}
    return add_tuples(pos, directions[direction]) 

def bishop(pos, direction, distance):
    directions = {'NE': (distance, distance), 'NW': (-1*distance, distance), 'SE': (distance, -1*distance), 'SW': (-1*distance, -1*distance)}
    return add_tuples(pos, directions[direction])

def queen(pos, direction, distance): 
    directions = {'N': (0, distance), 'NE': (distance, distance), 'NW': (-1*distance, distance), 
    'E': (distance, 0), 'SE': (distance, -1*distance), 'S': (0, -1*distance), 'W': (-1*distance, 0), 'SW': (-1*distance, -1*distance)}
    return add_tuples(pos, directions[direction])

def horse(pos, over, up):
    return add_tuples(pos, (over, up))


