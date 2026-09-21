import random

def display(board):
    
    print(f"\n {board[0]} | {board[1]} | {board[2]}    (0 | 1 | 2)")
    print("-----------    -----------")
    print(f" {board[3]} | {board[4]} | {board[5]}    (3 | 4 | 5)")
    print("-----------    -----------")
    print(f" {board[6]} | {board[7]} | {board[8]}    (6 | 7 | 8)\n")

def select_empty_position(board):
    empty_positions = [i for i, spot in enumerate(board) if spot == " "]
    return random.choice(empty_positions)

def check_row_column_diagonal(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

board = [" "] * 9
player = "X"

while " " in board:
    display(board)
    if player == "X":
        try:
            position = int(input("Enter position (0-8): "))
            if board[position] != " ":
                print("Position already taken! Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 0 and 8.")
            continue
        board[position] = "X"
    else:
        position = select_empty_position(board)
        print(f"Computer chooses position: {position}")
        board[position] = "O"
       
    if check_row_column_diagonal(board, player):
        display(board)
        print(player, "wins!")
        break
       
    if " " not in board:
        display(board)
        print("Game Draw!")
        break
       
    if player == "X":
        player = "O"
    else:
        player = "X"