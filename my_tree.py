from board import Board
import random
class Node:
    def __init__(self, item, left = None, right = None):
        self.data = item
        self.left = left
        self.right = right
        self.parent = None
        self.count = 0

class Tree:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""

        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s

        return recurse(self.root, 0)

    def help(self):
        check_result = self.root.data.check_board()
        position1 = random.choice(check_result)
        check_result.pop(check_result.index(position1))
        position2 = random.choice(check_result)
        check_result.pop(check_result.index(position2))
        right_board = Board([el for el in self.root.data.coors()])
        right_board.add(position1, "O")
        left_board = Board([el for el in self.root.data.coors()])
        left_board.add(position2, "O")

        def recur(node):
            if node.count != 0:
                node.count = node.left.count + node.right.count
                return node.count

            if type(node.data.check_board()) == int:
                node.count = node.data.check_board()
                return node.count

            else:
                check_result = node.data.check_board()
                if len(check_result) >= 2:
                    position1 = random.choice(check_result)
                    check_result.pop(check_result.index(position1))
                    pos_against1 = random.choice(check_result)
                    right_board = Board([el for el in node.data.coors()])
                    right_board.add(position1, "O")
                    right_board.add(pos_against1, "X")

                    position2 = random.choice(check_result)
                    check_result.pop(check_result.index(position2))
                    check_result.append(position1)
                    left_board = Board([el for el in node.data.coors()])
                    left_board.add(position2, "O")
                    pos_against2 = random.choice(check_result)
                    left_board.add(pos_against2, "X")

                    node.left = Node(left_board)
                    node.left.parent = node
                    node.right = Node(right_board)
                    node.right.parent = node
                    node.count += recur(node.left) + recur(node.right)
                    return node.count
                else:
                    position1 = random.choice(check_result)
                    board = Board([el for el in node.data.coors()])
                    board.add(position1, "O")
                    node.left = Node(board)
                    node.left.parent = node
                    recur(node.left)
                    return node.left.data.check_board()
        if recur(Node(right_board)) > recur(Node(left_board)):
            return position1
        else:
            return position2

if __name__ == "__main__":
    board = Board()
    board.add((1,1),"X")
    tr = Tree(Node(board))
    check_result = board.check_board()
    print(board)
    while type(board.check_board()) != int:
        my_move = tr.help()
        board.add(my_move, "O")
        free_moves = board.check_board()
        # print("Free : ", free_moves)
        print(board)
        coor1 = int(input("Row:"))
        coor2 = int(input("Col:"))
        board.add((coor1, coor2), "X")
    if board.check_board() == -1:
        print( "You won")
    elif board.check_board() == 1:
         print("You lost")
    else:
        print("Piece")