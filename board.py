class Board:
    def __init__(self):
        self.grid = []
        for r in range(3):
            row = []
            for c in range(3):
                row.append(" ")
            self.grid.append(row)

    def display(self):
        print("\nCurrent Board:")
        for i in range(3):
            print(" | ".join(self.grid[i]))
            if i < 2:
                print("-" * 9)
        print()

    def update_cell(self,row,col,symbol):
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False
    
    def check_winner(self,symbol):
        #rows
        for row in self.grid:
            if all(cell == symbol for cell in row):
                return True
            
        #columns
        for col in range(3):
            if all(self.grid[row][col] == symbol for row in range(3)):
                return True
            

        #diagonals
        if all(self.grid[i][i] == symbol for i in range(3)):
            return True
        if all(self.grid[i][2-i] == symbol for i in range(3)):
            return True
        
        return False
    
    def is_crowded(self):
        for row in self.grid:
            if " " in row:
                return False
        return True
    
    def reset(self):
        for r in range(3):
            for c in range(3):
                self.grid[r][c] = " "