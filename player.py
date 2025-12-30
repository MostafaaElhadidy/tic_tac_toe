class Player:
    def __init__(self,symbol):
        self.symbol = symbol

    def make_move(self,board):
        while True:
            try:
                row = int(input(f"Player {self.symbol}, enter your move row (1-3): ")) -1
                col = int(input(f"Player {self.symbol}, enter your move column (1-3): ")) -1
                if row not in range(3) or col not in range(3):
                    print("Invalid position, Please enter numbers between 1 and 3.")
                elif not board.update_cell(row,col,self.symbol):
                    print("Cell is already occupied, Please choose another one.")
                else:
                    break
            except ValueError:
                print("Invalid input, Please enter numbers only.")