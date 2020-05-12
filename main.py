import os

from board_class import Board

def main():
    board = Board()
    board.create()
    
    player = {
        'X': 0,
        'O': 0
    }

    # Gameloop
    clear_console()
    print("TIC-TAC-TOE\n")
    print(f"Score\nX: {player['X']}\nO: {player['O']}\n")
    board.print_board()
    
    input("Please enter cell number: ")
    input()

 
def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


if __name__ == "__main__":
    main()