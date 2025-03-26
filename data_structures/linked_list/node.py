class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        pass

    def set_next(self, node):
        self.next = node
        pass

    def __repr__(self):
        return self.val
