class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.parent = None
        self.item = item

    def getItem(self):
        return self.item

    def setLeft(self, next):
        self.left = next
    
    def setRight(self, next):
        self.right = next

    def setParent(self, next):
        self.parent = next

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getParent(self):
        return self.parent