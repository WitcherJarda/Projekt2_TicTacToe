"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Petr Svetr
email: petr.svetr@gmail.com
"""
from random import randint
import os
def game_rules():
    separator = "========================================"
    Rules = '''GAME RULES:
    Each player can place one mark (or stone)
    per turn on the 3x3 grid. The WINNER is
    who succeeds in placing three of their
    marks in a:
    * horizontal,
    * vertical or
    * diagonal row'''
    separator1 = "----------------------------------------"
    print(f"Welcome to Tic Tac Toe\n{separator}\n{Rules}\n{separator}\nLet's start the game\n{separator1}")

def create_game_board(board):
    print("+---+---+---+")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("+---+---+---+")
        
def insert_noughts(board):
    while True:
        try:
            user_choice = (input("Player O | Please enter coordinates in the format row/column (e.g., 0/0) "))
            cordinates = user_choice.split("/")
            row = int(cordinates[0])
            col = int(cordinates[1])
            if board[row][col] == "X" or board[row][col] == "O":
                print("The field is already occupied.")
            elif board[row][col] == " ":
                board[row][col] ="O"
                break
        except ValueError:
            print("Invalid value, enter coordinates as specified.")
        except IndexError:
            print("Out of range. Use coordinates 0-2 (e.g., 2/1).")
    board[row][col] = "O"
    
def insert_crosses (board):
    print("Computer X| Computer plays:")
    while True:
        random_nummer1 = randint(0,2)
        random_nummer2 = randint(0,2)
        if board[random_nummer1][random_nummer2] == " ":
            board[random_nummer1][random_nummer2] ="X"
            break

def control_the_game(board):
    win = "Congratulations, you won against the computer!"
    lose = "Computer wins!"
    for i in range(3):
        # Check line
        if board[i] == ["O", "O", "O"]:
            print(win)
            return True
        elif board[i] == ["X", "X", "X"]:
            print(lose)
            return True
            
        # Check columns
        if board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O":
            print(win)
            return True
        elif board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X":
            print(lose)
            return True
            
    # Check diagonals
    if (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or \
       (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"):
        print(win)
        return True
    if (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or \
       (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"):
        print(lose)
        return True
    # Check draw
    is_draw = True
    for row in board:
        for cell in row:
            if cell == " ":
                is_draw = False
                break
        if not is_draw:
            break
    if is_draw:
        print("It's a draw!")
        return True
        
def play_again():
    while True:
        try:
            again = input("Do you want to play again? (yes/no): ").strip().lower()
            if again not in ['yes', 'no']:
                raise ValueError("Invalid input. Please enter 'yes' or 'no'.")
            return again == 'yes'
        except ValueError as e:
            print(e)

def create_game():
    game_rules()
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    game_over = False
    create_game_board(board)


    while not game_over:
        insert_noughts(board)  
        create_game_board(board)  
        
        if control_the_game(board):  
            break  

        insert_crosses(board)  
        create_game_board(board)  

        if control_the_game(board):  
            break  
    print("Game over!")

    if play_again():
        os.system("cls")
        create_game()
    else:
        print("Thank you for playing!")

create_game()