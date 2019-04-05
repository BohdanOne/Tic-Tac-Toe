'''
This program is a simple Tic-Tac-Toe game
inspired by lesson in "Automate the Boring Stuff with Python"
'''
'''
TODO:
- game against computer
- choice of sign you want to play with
- optimize input for positions (ex. accepts lowercase)
- play the game in browser
'''
import random

messages = ['That is a good place to start!', 'Cool move.', 'Nicely done!', 'Smart!']

def print_board(board):
    print(board['A1'] + '|' + board['B1'] + '|' + board['C1'])
    print('-+-+-')
    print(board['A2'] + '|' + board['B2'] + '|' + board['C2'])
    print('-+-+-')
    print(board['A3'] + '|' + board['B3'] + '|' + board['C3'])

def winner():
    if (the_board['A1'] == the_board['A2']) and (the_board['A1'] == the_board['A3']) and (the_board['A1'] != ' '):
        return True
    if (the_board['B1'] == the_board['B2']) and (the_board['B1'] == the_board['B3']) and (the_board['B1'] != ' '):
        return True
    if (the_board['C1'] == the_board['C2']) and (the_board['C1'] == the_board['C3']) and (the_board['C1'] != ' '):
        return True
    if (the_board['A1'] == the_board['B1']) and (the_board['A1'] == the_board['C1']) and (the_board['A1'] != ' '):
        return True
    if (the_board['A2'] == the_board['B2']) and (the_board['A2'] == the_board['C2']) and (the_board['A2'] != ' '):
        return True
    if (the_board['A3'] == the_board['B3']) and (the_board['A3'] == the_board['C3']) and (the_board['A3'] != ' '):
        return True
    if (the_board['A1'] == the_board['B2']) and (the_board['A1'] == the_board['C3']) and (the_board['A1'] != ' '):
        return True
    if (the_board['C1'] == the_board['B2']) and (the_board['C1'] == the_board['A3']) and (the_board['C1'] != ' '):
        return True
    else:
        return False

# WELCOME MESSAGE

print('Let\'s start the game of Tic-Tac-Toe!')
print('Check out the board')
print()
print('A1|B1|C1')
print('--+--+--')
print('A2|B2|C2')
print('--+--+--')
print('A3|B3|C3')
print()
print('Let\'s play!')

# THE GAME

game_is_on = 'Y'

while game_is_on == 'Y':
    the_board = {'A1': ' ', 'B1': ' ', 'C1': ' ',
                 'A2': ' ', 'B2': ' ', 'C2': ' ',
                 'A3': ' ', 'B3': ' ', 'C3': ' '}
    turn = 'X'
    start = 0
    while ' ' in the_board.values():  
        print()
        move = input('It\'s {} turn. Where do you want to place your {}? '.format(turn,turn))
        if move not in the_board.keys():
            print('Look at the board again.\nYou can choose from: A1, A2, A3, B1, B2, B3, C1, C2, C3')
            continue
        elif the_board[move] == 'X' or the_board[move] == 'O':
            print('{} already there! Choose other position. '.format(the_board[move]))
        else:     
            the_board[move] = turn
            print_board(the_board)
            if winner():
                print('{} wins! Congratulations!'.format(turn))
                break
            else:
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
            if start == 0:
                print(messages[0])
            else:
                print(messages[random.randint(1, len(messages)-1)])
            start = 1          
    print('Game is over')
    game_on = input('Press Y if you want to play again.')
