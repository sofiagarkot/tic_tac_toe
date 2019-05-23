from board import Board
from my_tree import Tree, Node

moves = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1,0), 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2]}
board = Board()
tr = Tree(Node(board))
while type(board.check_board()) != int:
    user_move = int(input("Enter number from 1 to 9 : "))
    coor = moves[user_move]
    try:
        if board.right_position(user_move):
            board.add((coor[0], coor[1]), "X")
    except TypeError:
        response = input("Invalid input! Do you want to continue? Type <yes> or <no> : ")
        if response.lower() == "yes":
            continue
        else:
            break
    print(board)
    if board.check_board() == -1:
        print("You won")
        break
    elif board.check_board() == 1:
        print("You lost")
        break
    elif board.check_board() == 0:
        print("Piece")
        break

    my_move = tr.help()
    board.add(my_move, "O")
    print("Computer's move : ")
    print(board)

    if board.check_board() == -1:
        print("You won")
        break
    elif board.check_board() == 1:
        print("You lost")
        break
    elif board.check_board() == 0:
        print("Piece")
        break
