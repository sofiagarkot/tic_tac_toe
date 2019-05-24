class Node:
    def __init__(self, item, left = None, right = None):
        self.data = item
        self.left = left
        self.right = right
        self.parent = None
        self.count = 0