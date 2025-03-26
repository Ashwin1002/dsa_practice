from stack import Stack

class DebounceStack(Stack):

    def __init__(self):
        super().__init__()

    def push(self, item):
        if self.peek() != item:
            super().push(item)
    pass
