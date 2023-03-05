from battleship import *
def menu_battleship():
    print_ship()
    time.sleep(4)
    clear()
    board_size= int(input_with_quit("Welcome to Battleship game!\nDuring all game you can quit game writnig \"quit\" \n \nEnter board size (5-10): "))
    if 5<=board_size<=10:
        if board_size==10:
            ship_size=[1,1,1,1,2,2,2,3,3,4]
        elif board_size==9:
            ship_size=[1,1,1,1,2,2,2,3,3]
        elif board_size==8:
            ship_size=[1,1,1,1,2,2,2,3]
        elif board_size==7:
            ship_size=[1,1,1,2,2,3]
        elif board_size==6:
            ship_size=[1,1,2,3]
        elif board_size==5:
            ship_size=[1,1,1,2] 
        choice=menu_choice()
        return board_size,ship_size,choice
    else:
        print ("Invalid input! (must be between 5-10)")
        time.sleep(1)
        return menu_battleship()

def menu_choice():
    clear()
    choice= int(input_with_quit("1. Single player \n2. Multiplayer\n Choose options: "))
    if choice ==1 or choice ==2:
        return choice  
    else:
        print ("Invalid input! (must be 1 or 2)")
        time.sleep(1)
        return menu_choice()
