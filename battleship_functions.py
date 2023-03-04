from os import system,name
import time

def clear(): 
    if name=='nt':
        _ = system('cls')
    else:
        _ = system('clear')

# Function to create an empty board of given size
def create_board(size):
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        board.append(row)
    return board

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

# Function to get user input for placing a ship
def get_ship_placement(board, size):
    while True:
        try:
            move = input(f"Enter the row (A-{chr(65+len(board)-1)}) and column (1-{len(board)}) for a ship of size {size}: ")
            move= move_check_syntax(move)
            while move==False:
                move = input(f"Enter the row (A-{chr(65+len(board)-1)}) and column (1-{len(board)}) for a ship of size {size}: ")                
            row = move[0]
            col = move[1]
            if size !=1:
                direction = input("Enter the direction (\"h\"- horizontal, \"v\"- vertical): ")
            else:
                direction="v"
            clear()
            if direction not in ["h", "v","V","H"]:
                raise ValueError
            if not can_place_ship(board, row, col, direction, size):
                print("Ships are too close or go out of the board!")
                get_ship_placement(board, size)
                return row, col, direction
            
            return row, col, direction
        except (ValueError, IndexError):
            print("Invalid input! Try again.")

# Function to check user input for placing a ship
def move_check_syntax(move = False):
    if len(move) != 2: return False
    move = move.lower()
    if move[0] in ["a", "b", "c"] and move[1] in ["1", "2", "3"]:
        move = move.replace("a", "1")
        move = move.replace("b", "2")
        move = move.replace("c", "3")
        return [int(move[0])-1, int(move[1])-1]
    elif move[0] in ["1", "2", "3"] and move[1] in ["a", "b", "c"]:
        move = move[::-1]
        move = move.replace("a", "1")
        move = move.replace("b", "2")
        move = move.replace("c", "3")
        return [int(move[0])-1, int(move[1])-1]
    else: return False

# function to check if a ship can be placed at the given position and direction
def can_place_ship(board, row, col, direction, size):
    if direction.lower == "h":
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
    elif direction.lower == "v":
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
    if direction.lower == "h":
        for j in range(col, col+size):
            board[row][j] = "X"
    elif direction.lower == "v":
        for i in range(row, row+size):
            board[i][col] = "X"

# Function to get user input for shooting
def get_shot_position(board):
    while True:
        try:
            shot = input(f"Enter the row (A-{chr(65+len(board)-1)}) and column (1-{len(board)}) to shoot: ")
            shot= move_check_syntax(shot)
            while shot==False:
                shot = input(f"Enter the row (A-{chr(65+len(board)-1)}) and column (1-{len(board)}) to shoot: ")                
            row = shot[0]
            col = shot[1]
            
            if not (0 <= row < len(board) and 0 <= col < len(board[0])):
                raise (ValueError)
            if board[row][col] in ["H", "M"]:
                raise (ValueError)
            return row, col
        except (ValueError, IndexError):
            print("Invalid input! Try again.")

# function to check if a given shot hits a ship
def check_shot(player_board_shooting, board, row, col):
    if board[row][col] == "X":
        player_board_shooting[row][col] = "H"
        board[row][col] = "H"
        clear()
        if all_sunk(board):
            return False
        if is_sunk(player_board_shooting, row, col):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if player_board_shooting[i][j] == "H":
                        player_board_shooting[i][j] = "S"
            print("You've sunk a ship!")
        else:
            print("You've hit a ship!")
        display_board(player_board_shooting)
        return True
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
def is_sunk(player_board_shooting, row, col):
    size = 1
    if player_board_shooting[row][col] == "X":
        # Check horizontally
        i = col - 1
        while i >= 0 and player_board_shooting[row][i] == "X":
            size += 1
            i -= 1
        i = col + 1
        while i < len(player_board_shooting) and player_board_shooting[row][i] == "X":
            size += 1
            i += 1
        if size >= 3:
            return True

        # Check vertically
        size = 1
        i = row - 1
        while i >= 0 and player_board_shooting[i][col] == "X":
            size += 1
            i -= 1
        i = row + 1
        while i < len(player_board_shooting) and player_board_shooting[i][col] == "X":
            size += 1
            i += 1
        if size >= 3:
            return True
    return False

# function to check if all ships are sunk
def all_sunk(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "X":
                return False
    return True

# function to play game
def play_game(board_size, ship_sizes):
    board = create_board(board_size)
    for size in ship_sizes:
        row, col, direction = get_ship_placement(board, size)
        place_ship(board, row, col, size, direction)
        display_board(board)
    if input("Press enter to continue or q to quit: ") == "q":
        print("Thank you game! Bay :(")
        exit
    return board

# function to shooti
def shooting(player_board_shooting,board, player_active):
    print("Let's start shooting!")
    row, col = get_shot_position(player_board_shooting)
    if check_shot(player_board_shooting,board, row, col):       
        shooting(player_board_shooting,board, player_active)
    else:
        print(f"Congratulations! You've sunk all the ships! \n Winner is {player_active}")
        exit()