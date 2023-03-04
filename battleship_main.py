from battleship import *
from battleship_menu import *

settings=menu_battleship()
board_size=settings[0]
ship_size=settings[1]
choice=settings[2]

player_active = 1
first_player_board=play_game(board_size,ship_size)
clear()
second_player_board=play_game(board_size,ship_size)
clear()

first_player_board_shooting=create_board(board_size)
second_player_board_shooting=create_board(board_size)

while True:
    print("active player is 🚢",player_active)
    if player_active == 1: 
        shooting(first_player_board_shooting,second_player_board, player_active)
        player_active = 2
    else:
        shooting(second_player_board_shooting,first_player_board, player_active) 
        player_active = 1