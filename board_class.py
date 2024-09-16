class Board:
    # Initializer
    def create(self):
        self.content = list(range(1, 10))
    
    def print_board(self):
        b = self.content
        border = '+---+---+---+'

        print(border)
        print(f"| {b[0]} | {b[1]} | {b[2]} |\n{border}")
        print(f"| {b[3]} | {b[4]} | {b[5]} |\n{border}")
        print(f"| {b[6]} | {b[7]} | {b[8]} |\n{border}\n")

    def update_board(self, cell, player):
        if self.content[cell-1] not in ['X', 'O']:  # Check if the cell is available
            self.content[cell-1] = player
            return True
        return False

    def check_winner(self):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]  # Diagonal
        ]
        
        for condition in win_conditions:
            if self.content[condition[0]] == self.content[condition[1]] == self.content[condition[2]]:
                return self.content[condition[0]]
        if all(isinstance(x, str) for x in self.content):  # Check if all cells are filled
            return 'Tie'
        return None  # Game continues
