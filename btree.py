from board import Board
import random
from btnode import Node

class Tree:
    def __init__(self, root=None):
        self.root = root

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