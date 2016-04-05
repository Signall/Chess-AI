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

'''
Data Structure
 0 1 2 3 4 5 6 7
0
1
2
3
4
5
6
7
'''
