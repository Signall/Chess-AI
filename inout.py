def write_board(array):
    with open('board.csv', 'w') as f:
        for line in array:
            f.write(str(line) + '\n')

def read_board():
    array = []
    with open('board.csv', 'r') as f:
        for line in f:
            array.append(line.replace('\n', '').split(', '))

    return array

