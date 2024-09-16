# Tic-Tac-Toe Python Game

## Description

This project is a simple implementation of the classic **Tic-Tac-Toe** game using Python. It is designed for two players, 'X' and 'O', to play against each other in a terminal/console. The game checks for win conditions, ties, and allows players to restart the game if desired.

## Features

- Two-player mode: 'X' and 'O' take turns to play.
- Board is displayed dynamically after each move.
- Input validation ensures valid moves.
- Win conditions and ties are checked automatically.
- Score tracking for both players.
- Option to play multiple rounds.

## How to Run

1. Clone or download the repository to your local machine.
2. Ensure that you have Python 3 installed.
3. Open a terminal or command prompt and navigate to the folder containing the project files.
4. Run the `main.py` file to start the game:
    ```bash
    python main.py
    ```

## File Structure

- `board_class.py`: Contains the `Board` class, which manages the game board and game logic, including move validation and win conditions.
- `main.py`: Contains the main game loop, where player input is processed, and the game flow is controlled.

## How to Play

1. **Start the game** by running `main.py`.
2. **Take turns**: Players 'X' and 'O' take turns selecting a numbered cell on the 3x3 board.
3. **Winning the game**: The first player to get 3 in a row horizontally, vertically, or diagonally wins the game.
4. **Tie**: If all cells are filled and no player has won, the game is declared a tie.
5. **Play again**: After each game, players are given the option to play again.

## Example Game Flow

```bash
TIC-TAC-TOE

Score
X: 0
O: 0

+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+

Player X, enter cell number (1-9):
```

## Future Improvements
- Add an option for single-player mode against an AI.
- Improve the UI/UX by adding a graphical interface (GUI).
- Implement additional game modes (e.g., 4x4 or larger grids).
