import random
import os
from art import logo
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
winning_scenarios = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}]
blank_cells = [val for val in range(9)]
player_set = set()
computer_set = set()


def display_board():
    for i in range(0, 9, 3):
        print('   |   |   ')
        print(f' {board[i]} | {board[i+1]} | {board[i+2]} ')
        print('   |   |   ')
        if i != 6:
            print('-----------')
        else:
            print("\n")


def choose_symbol():
    while True:
        user_choice = input('Please select your symbol: X or O\n')
        if user_choice == 'X':
            return 'X', 'O'
        elif user_choice == 'O':
            return 'O', 'X'
        else:
            print('You have not given the correct input.')


def player_chance():
    while True:
        try:
            cell = int(input('Choose the cell you want to play in (0-8)\n'))
        except ValueError:
            print('You have not given correct input.')
            continue

        if cell not in range(9) or board[cell] != ' ':
            print('Please choose again.')
        else:
            board[cell] = player_symbol
            blank_cells.remove(cell)
            player_set.add(cell)
            os.system('cls')
            return


def computer_chance():
    cell = random.choice(blank_cells)
    board[cell] = computer_symbol
    blank_cells.remove(cell)
    computer_set.add(cell)
    print(f'Computer has played at cell: {cell}')
    display_board()


def check_for_win(is_player):
    for check_set in winning_scenarios:
        if is_player == 0 and check_set.issubset(player_set):
            display_board()
            print("You have won.")
            return True
        elif is_player == 1 and check_set.issubset(computer_set):
            print("Computer has won.")
            return True
    return False


def check_for_game_over():
    return ' ' not in board


print(logo)
print('Welcome to the Tic Tac Toe Game.')
player_symbol, computer_symbol = choose_symbol()
display_board()

chance = random.randint(0, 1)
if chance == 0:
    print('You play first.')
else:
    print('Computer play first.')


game_over = check_for_win(chance)

while not game_over:

    if not check_for_game_over():
        if chance == 0:
            player_chance()
            game_over = check_for_win(chance)
            chance = 1
        else:
            computer_chance()
            game_over = check_for_win(chance)
            chance = 0
    else:
        print(' GAME OVER ')
        game_over = True






