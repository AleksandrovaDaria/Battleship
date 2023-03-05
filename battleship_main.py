from battleship import *
from battleship_menu import *

settings=menu_battleship()
board_size=settings[0]
ship_size=settings[1]
choice=settings[2]

player_active = 1

first_player_board_shooting=create_board(board_size)
second_player_board_shooting=create_board(board_size)

if choice==2:
    first_player_board=play_game(board_size,ship_size)
    clear()
    second_player_board=play_game(board_size,ship_size)
    clear()
    while True:
        print("active player is ",player_active)
        if player_active == 1: 
            shooting(first_player_board_shooting,second_player_board, player_active,board_size)
            if all_sunk(second_player_board):   
                print(f"Congratulations! You've sunk all the ships! \n Winner is player {player_active}")
                print_ship()
                exit()
            player_active = 2
        else:
            shooting(second_player_board_shooting,first_player_board, player_active,board_size) 
            if all_sunk(first_player_board):
                print(f"Congratulations! You've sunk all the ships! \n Winner is player {player_active}")
                print_ship()
                exit()
            player_active = 1
elif choice==1:
    first_player_board=play_game(board_size,ship_size)
    clear()
    ai_play_board=ai_play_game(board_size,ship_size)
    clear()
    while True:
        if player_active == 1: 
            print("active player is ",player_active)
            shooting(first_player_board_shooting,ai_play_board, player_active,board_size)
            if all_sunk(ai_play_board):
                print(f"Congratulations! You've sunk all the ships! \n Winner is player {player_active}")
                print_ship()
                exit()
            player_active = 2
        else:
            print("AI is playing now")
            time.sleep(1)  
            shooting_ai(second_player_board_shooting,first_player_board, player_active,board_size)
            time.sleep(1)
            if all_sunk(first_player_board,):
                print(f"Congratulations! You've sunk all the ships! \n Winner is AI!")
                print_ship()
                exit()
            player_active = 1