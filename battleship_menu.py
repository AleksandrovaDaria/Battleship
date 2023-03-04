from battleship import *
def menu_battleship():
    clear()
    try:
        board_size= int(input("Enter board size (5-10): "))
    except:
        print ("Invalid input! (must be between 5-10)")
        time.sleep(1)
        return menu_battleship()

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
    try:
        choice= int(input("1. Single player \n2. Multiplayer\n Choose options: "))
    except:
        print ("Invalid input! (must be 1 or 2)")
        time.sleep(1)
        return menu_choice()

    if choice ==1 or choice ==2:
        return choice  
    else:
        print ("Invalid input! (must be 1 or 2)")
        time.sleep(1)
        return menu_choice()
