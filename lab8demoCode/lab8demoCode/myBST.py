from myBSTNode import Node

class myBST:
    def __init__(self, root = None):
        self.root = root
        self.list = []

    def insert(self, item):
        x = self.root
        y = None
        while (x != None):
            y = x
            if (item < x.getItem()):
                x = x.getLeft()
            else:
                x = x.getRight()
        newNode = Node(item)
        newNode.setParent(y);
        if (y == None):
            self.root = newNode
        else:
            if (item < y.getItem()):
                y.setLeft(newNode)
            else:
                y.setRight(newNode)

    def inOrder(self, n):
        if (n!= None):
            self.inOrder(n.getLeft())
            self.visit(n)
            self.inOrder(n.getRight())

    def visit(self, n):
        print(n.getItem())
        self.list.append(n.getItem())
    
    def getList(self):
        return self.list

    def clearList(self):
        self.list = []

    def getRoot(self):
        return self.root