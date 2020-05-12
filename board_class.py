class Board:
    # Attribute
    content = []
    
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