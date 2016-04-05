import inout as io

DIRECTIONS = ['N', 'S', 'E', 'W']
OTHER_DIRECTIONS = ['NE', 'NW', 'SE', 'SW']
ALL_DIRECTIONS = DIRECTIONS + OTHER_DIRECTIONS

PIECES = ['pawn', 'king', 'castle', 'bishop', 'queen', 'horse']

def find_pos(piece, color):
    assert color.upper() == "W" or color.upper == "B", "Color isn\'t black or white!"
    assert piece.lower() in PIECES
    piece_name = str(color + piece).upper()

    board = io.read_board()
    
    positions = []

    for line_num, line in enumerate(board, 1):
        # Start from the top and go down.
        for x, piece_type in enumerate(line, 1):
            # Start at left then go right for line numbering purposes.
            if piece_type == piece_name:
                positions.append((x, line_num))

    return positions


def find_piece(pos):
    x, y = pos[0], pos[1]
    board = io.read_board()
    return board[y][x]


