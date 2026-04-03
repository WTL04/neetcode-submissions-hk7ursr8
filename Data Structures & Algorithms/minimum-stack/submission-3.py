class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] # tracks min element in self.stack
        self.currentMin = float("inf")
        

    def push(self, val: int) -> None:
        self.currentMin = min(val, self.currentMin)
        self.minStack.append(self.currentMin)
        self.stack.append(val)

    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()

        # reset the currentMin to the top of minStack
        self.currentMin = self.minStack[-1] if self.minStack else float("inf")

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
