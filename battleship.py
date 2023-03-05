from os import system,name
import time
import random

def clear():
    if name=='nt':
        _ = system('cls')
    else:
        _ = system('clear')

# function to display the board
def display_board(board):
    print("   ", end="")
    for i in range(len(board)):
        print(i+1, end=" ")
    print()
    for i in range(len(board)):
        print(chr(i+65), end="  ")
        for j in range(len(board[i])):
            print(board[i][j], end=" ")
        print()

# function to check if a ship can be placed at the given position and direction
def can_place_ship(board, row, col, direction, size):
    if direction == "h":
        if col + size > len(board[0]):
            return False
        for j in range(col, col+size):
            if board[row][j] != 0:
                return False
            if row > 0 and board[row-1][j] != 0:
                return False
            if row < len(board)-1 and board[row+1][j] != 0:
                return False
        return True
    elif direction == "v":
        if row + size > len(board):
            return False
        for i in range(row, row+size):
            if board[i][col] != 0:
                return False
            if col > 0 and board[i][col-1] != 0:
                return False
            if col < len(board[0])-1 and board[i][col+1] != 0:
                return False
        return True

# function to place a ship at the given position and direction
def place_ship(board, row, col, size, direction):
    if direction == "h":
        for j in range(col, col+size):
            board[row][j] = "X"
    elif direction == "v":
        for i in range(row, row+size):
            board[i][col] = "X"

# function to check if a given shot hits a ship
def check_shot(player_board_shooting, board, row, col,board_size):
    if board[row][col] == "X":
        player_board_shooting[row][col] = "H"
        board[row][col] = "H"
        clear()
        if all_sunk(board):
            return False
        if is_sunk(board, row, col, board_size):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if player_board_shooting[i][j] == "H":
                        player_board_shooting[i][j] = "S"
            print("You've sunk a ship!")
        else:
            print("You've hit a ship!")
        display_board(player_board_shooting)
        return board
    elif board[row][col] == 0:
        player_board_shooting[row][col] = "M"
        clear()
        print("You've missed!")
        display_board(player_board_shooting)
        time.sleep(2)
        clear()
        return False
    else:
        print("You've already shot there!")
        return True

# Function to check if a ship is sunk after a hit
def is_sunk(player_board_shooting, row, col,board_size):
    iterator=0
    if player_board_shooting[row][col] == "H":
        if col-1>0:
            if player_board_shooting[row][col-1] == "X":
                iterator+=1
        if col+1<=board_size:
            if player_board_shooting[row][col+1] == "X":
                iterator +=1
        if row+1<=board_size:  
            if player_board_shooting[row+1][col] == "X":
                iterator+=1
        if row-1>0:
            if player_board_shooting[row-1][col] == "X":
                iterator+=1
    if iterator !=0:
        return False
    else:
        return True

# function to check if all ships are sunk
def all_sunk(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "X":
                return False
    return True

# Function to create an empty board of given size
def create_board(size):
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        board.append(row)
    return board


# Function to get user input for placing a ship
def get_ship_placement(board, size):
    while True:
        try:
            position = input_with_quit(f"Enter the row (A-{chr(65+len(board)-1)}) and column (1-{len(board)}) for a ship of size {size}: ")
            row = ord(position[0]) - 65
            col = int(position[1:]) - 1
            if size !=1:
                direction = input_with_quit("Enter the direction (h/v): ")
            else:
                direction="v"
            clear()
            if direction not in ["h", "v"]:
                raise ValueError
            if not can_place_ship(board, row, col, direction, size):
                print("Ships are too close or go out of the board!")
                return get_ship_placement(board, size)
            return row, col, direction
        except (ValueError, IndexError):
            print("Invalid input! Try again.")

# Function to get user input for shooting
def get_shot_position(board):
    while True:
        try:
            position = input_with_quit(f"Enter the row (A-{chr(65+len(board)-1)}) and column (1-{len(board)}) to shoot: ")
            row = ord(position[0]) - 65
            col = int(position[1:]) - 1
            if not (0 <= row < len(board) and 0 <= col < len(board[0])):
                raise (ValueError)
            if board[row][col] in ["H", "M"]:
                raise (ValueError)
            return row, col
        except (ValueError, IndexError):
            print("Invalid input! Try again.")

def play_game(board_size, ship_sizes):
    board = create_board(board_size)
    for size in ship_sizes:
        row, col, direction = get_ship_placement(board, size)
        place_ship(board, row, col, size, direction)
        display_board(board)
    if input("Press enter to continue or \"quit\" to quit: ") == "quit":
        print("Thank you for game! Bay :(")
        exit
    return board

def shooting(player_board_shooting,board, player_active,board_size):
    print("Let's start shooting!")
    row, col = get_shot_position(player_board_shooting)
    if not all_sunk(board):
        if check_shot(player_board_shooting,board, row, col,board_size):       
            return shooting(player_board_shooting,board, player_active,board_size)
    else:
        print(f"Congratulations! You've sunk all the ships! \n Winner is player {player_active}")
        exit()

def ai_play_game(board_size, ship_sizes):
    board = create_board(board_size)
    for size in ship_sizes:
        row = random.randint(0,board_size-1)
        col= random.randint(0,board_size-1)
        direction=random.choice(("v", "h"))
        if can_place_ship(board, row, col, direction, size):
            place_ship(board, row, col, size, direction)
        else:
            return ai_play_game(board_size, ship_sizes)
    display_board(board)
    if input_with_quit("Press enter to continue or \"quit\" to quit: ") == "quit":
        print("Thank you for game! Bay :(")
        exit
    return board

def shooting_ai(player_board_shooting,board, player_active,board_size):
    row = random.randint(0,board_size-1)
    col= random.randint(0,board_size-1)
    if not all_sunk(board):
        if check_shot(player_board_shooting,board, row, col,board_size):       
            return shooting_ai(player_board_shooting,board, player_active,board_size)
    else:
        print(f"Congratulations! You've sunk all the ships! \n Winner is player {player_active}")
        exit()

def input_with_quit(question = ""):
    answer = input(question)
    if answer.lower() == "quit":
        print("Thank you for game! Bay :(")
        exit()
    return answer