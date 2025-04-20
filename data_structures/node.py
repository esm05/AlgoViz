 # A node class for data structures.

class Node:
    def __init__(self, value, x=0, y=0, next_node=None):
        self.value = value
        self.x = x
        self.y = y
        self.next = next_node
        self.left = None
        self.right = None