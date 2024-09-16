import os
from board_class import Board

def main():
    board = Board()
    board.create()
    
    player = {
        'X': 0,
        'O': 0
    }
    current_player = 'X'
    
    # Game loop
    while True:
        clear_console()
        print("TIC-TAC-TOE\n")
        print(f"Score\nX: {player['X']}\nO: {player['O']}\n")
        board.print_board()
        
        # Player move
        cell = int(input(f"Player {current_player}, enter cell number (1-9): "))
        if cell < 1 or cell > 9 or not board.update_board(cell, current_player):
            print("Invalid move. Try again.")
            input("Press Enter to continue...")
            continue
        
        # Check if there's a winner or tie
        result = board.check_winner()
        if result:
            clear_console()
            board.print_board()
            if result == 'Tie':
                print("It's a tie!")
            else:
                print(f"Player {result} wins!")
                player[result] += 1  # Update the score
            if input("Play again? (y/n): ").lower() != 'y':
                break
            board.create()  # Reset the board
            current_player = 'X'  # Reset to player X
            continue
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

 
def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


if __name__ == "__main__":
    main()
