class Board:
    '''
    class for representation of a board
    '''
    def __init__(self, coors = []):
        self._board = [[" " for j in range(3)] for i in range(3)]
        self.line_board = [" " for i in range(9)]
        self.last_turn = (None, None)
        for coor in coors:
            self.add(coor[0], coor[1])

    def right_position(self, num):
        if 1<=num<=9:
            if self.line_board[num - 1] == " ":
                return True
        raise TypeError("Position is busy!")


    def check_board(self, sign="O"):
        possible_win_states = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9)]
        for state in possible_win_states:
            if self.line_board[state[0] - 1] == self.line_board[state[1] - 1] == self.line_board[state[2] - 1] == "O":
                return 1
            elif self.line_board[state[0] - 1] == self.line_board[state[1] - 1] == self.line_board[state[2] - 1] == "X":
                return -1
        if not " " in self.line_board:
            return 0
        else:
            res = []
            for coor in [(i,j) for i in range(3) for j in range(3)]:
                if self._board[coor[0]][coor[1]] == " ":
                    res.append(coor)
            # повертати список вільних клітинок
            return res

    def coors(self):
        res = []
        for coor in [(i, j) for i in range(3) for j in range(3)]:
            if self._board[coor[0]][coor[1]] != " ":
                res.append((coor,self._board[coor[0]][coor[1]]))
        return res

    def add(self, coor, sign):
        if 0 <= coor[0] <= 2 and 0 <= coor[1] <= 2:
            if self._board[coor[0]][coor[1]] == " ":
                self._board[coor[0]][coor[1]] = sign
                self.line_board[coor[0]*3+coor[1]] = sign
        else:
            raise IndexError("Coordinates are out of field")

    def __str__(self):
        res = "\n"
        for el in self._board:
            res +="|"
            for l in el:
                res += l+"|"
            res += "\n"
        return res

if __name__ == "__main__":
    my_board = Board()
    my_board.add((1,1), "O")
    my_board.add((2,1), "X")
    my_board.add((0,0), "O")
    # my_board.add((2,2), "O")
    print(my_board.check_board())
    print(my_board)



