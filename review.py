

## list -  order matters

fam = ["Tom", "Carole", "Baby Brooke"]

fam2 = ["Carole", "Tom", "Baby Brooke"]

fam == fam2

## dictionary Order doesn't matter

fam = {'husband': 'Tom', 'wife': 'Carole', 'grand_baby': 'Baby Brooke'}

fam2 = {'wife': 'Carole', 'grand_baby': 'Baby Brooke', 'husband': 'Tom'}

fam == fam2

1. ## print the keys in fam


2. ## print the values in fam

3. work through the tic tac toe board page 113 

# Tic Tac Toe  Board

theBoard = {'top-L': ' ', 'top-M':' ', 'top-R':' ',
            'mid-L': ' ', 'mid-M':' ', 'mid-R':' ',
            'low-L': ' ', 'low-M':' ', 'low-R':' '}


def printBoard(board):
    print(' '+ board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'x'
for i in range(9):
    print('Turn for ' + turn + '_ on which space? ')
    move = input()
    theBoard[move] = turn
    if turn == 'x':
        turn = '0'
    else:
        turn = 'x'

printBoard(theBoard)


