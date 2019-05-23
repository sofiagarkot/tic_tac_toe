class Board :
    NOUGHT = 1
    CROSS = -1
    EMPTY = 0
    WINNING_COMBINATIONS = [((0,0), (0,1), (0,2))]
    def __init__(self):
        self.cells = [[0]*3 for i in range(3)]

    # def generate_winning_combinations:
    def make_move(self, cell, move):
        if self.cells[cell[0]][cell[1]] != 0:
            return False
        self.cells[cell[0]][cell[1]] = move
        return True

    def has_winner(self):
        for combination in self.WINNING_COMBINATIONS:
            lst = []
            for cell in combination:
                lst.append(self.cells[cell[0]][cell[1]])
            if max(lst) == min(lst) and max(lst) != 0:
                return max(lst)
        return 0

    def __str__(self):
        transform = {0:" ", 1:"X", 2:"O"}
        return "\n".join([" ".join(map(lambda x : transform[x], row)) for row in self.cells])

    def make_random_mov(self):
        for i in range(3):
            for j in range(3):
                pass

if __name__ == "__main__":
    board = Board()
    print(board)