class myQueue:
    def __init__(self):
        self.content = []

    def empty(self):
        return len(self.content) == 0

    def push(self, item):
        self.content.append(item)

    def pop(self):
        if self.empty():
            return "Is empty"
        return self.content.pop(0)

    def contents(self):
        return self.content