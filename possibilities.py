import inout as io
import pieces as pc

import random

DIRECTIONS = ['N', 'S', 'E', 'W', 'NE', 'NW', 'SE', 'SW']
PIECES = ['pawn', 'king', 'castle', 'bishop', 'queen', 'horse']

def find(piece, color):
    assert color.casefold() == "W".casefold() or color.casefold() == "B".casefold()
    assert piece.lower() in PIECES
    piece_name = str(color + piece).upper()

    positions = []
    line_number = 8
    piece_number = 8
    for line in io.read_board():
        for __piece in line:
            if __piece == piece_name:
                piece_number -= 1
                positions.append((piece_number, line_number))
                
            piece_number -= 1
        line_number -= 1
        piece_number = 8
    return positions

def find_color(color):
    assert color.casefold() == "W".casefold() or color.casefold() == "B".casefold()
    return [find(piece, color) for piece in PIECES]
        

def posibilities(piece):
    pieces = {'king': pc.king, 'castle': pc.castle, 'bishop': pc.bishop, 'queen': pc.queen, 'horse': pc.horse}
    
    if piece == 'king':
        moves = [pc.king(pos, direction) for direction in DIRECTIONS]
        
    elif piece == 'castle':
        moves = [pc.castle(pos, direction, distance) for direction in DIRECTIONS for distance in range(9)]

    elif piece == 'bishop':
        moves = [pc.bishop(pos, direction, distance) for direction in DIRECTIONS - ['N', 'S', 'E', 'W'] for distance in range(9)]


print(find_color('W'))
print(find('KING', 'W'))
