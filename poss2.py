import find
from pieces import *

from itertools import permutations

DIRECTIONS = ['N', 'S', 'E', 'W']
OTHER_DIRECTIONS = ['NE', 'NW', 'SE', 'SW']
ALL_DIRECTIONS = DIRECTIONS + OTHER_DIRECTIONS
MAX_DIST = range(1, 9)
HORSE_MOVES = permutations((3, 2, -3, -2), 2)
COLORS = ['B', 'W']

PIECES = ['pawn', 'king', 'castle', 'bishop', 'queen', 'horse']

def strip_color(piece):
    """ Strips color prefix "W" or "B" off of name """
    return piece[1:]

def in_bounds(pos):
    return all([p >= 0 for p in pos])

def max_dist_in_direction(pos, direction):
    for i, distance in enumerate(range(0, 9)):
        directions = {'N': (0, distance), 'NE': (distance, distance), 'NW': (-1*distance, distance),
        'E': (distance, 0), 'SE': (distance, -1*distance), 'S': (0, -1*distance), 'W': (-1*distance, 0), 'SW': (-1*distance, -1*distance)}
        if find.find_piece(add_tuples(pos, directions[direction])) == 'None':
            if i >= len(range(0, 9)):
                return distance 
        else:
            return distance
        

def possibilities(pos):
    piece = find.find_piece(pos)
    piece_color = piece[0]
    gen_piece = strip_color(piece) # Generic Piece
    
    possible_moves = []

    if gen_piece.casefold() == "pawn".casefold():
        for color in COLORS:
            move = pawn(pos, color)
            if in_bounds(move):            
                possible_moves.append(move)

    elif gen_piece.casefold() == "king".casefold():
        for direction in ALL_DIRECTIONS:
            move = king(pos, direction)
            if in_bounds(move):
                if find.find_piece(move) == 'None' or find.find_piece(move)[0] is not piece_color:
                    possible_moves.append(move)
                    
    elif gen_piece.casefold() == "castle".casefold():
        for direction in DIRECTIONS:
            for distance in MAX_DIST:
                move = castle(pos, direction, distance)
                if in_bounds(move):
                    if find.find_piece(move) == 'None' or find.find_piece(move)[0] is not piece_color:
                        possible_moves.append(move)

    elif gen_piece.casefold() == "queen".casefold():
        for direction in ALL_DIRECTIONS:
            for distance in MAX_DIST:
                possible_moves.append(queen(pos, direction, distance))

    elif gen_piece.casefold() == "horse".casefold():
        for horse_direction in HORSE_DIRECTIONS:
            possible_moves.append(horse(pos, *horse_direction))

    elif gen_piece.casefold() == "bishop".casefold():
        for direction in OTHER_DIRECTIONS:
            for distance in MAX_DIST:
                move = bishop(pos, direction, distance)
                if find.find_piece(move) == 'None' or find.find_piece(move)[0] is not piece_color:
                    possible_moves.append(move)

    return possible_moves

if __name__ == '__main__':
    pos1 = int(input('Pos 1 '))
    pos2 = int(input('Pos 2 '))
    pos = (pos1, pos2)
    print(possibilities(pos))
