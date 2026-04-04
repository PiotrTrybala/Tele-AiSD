
from queue import Queue


def _level_traversal(node):
    q = Queue()
    q.put(node)
    while not q.empty():
        n = q.get()
        print(n.value)
        if n.left:
            q.put(n.left)
        if n.right:
            q.put(n.right)

def _inorder_traversal(node):
    if not node:
        return
    _inorder_traversal(node.left)
    print(node.value)
    _inorder_traversal(node.right)

class BstNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, x):

        if self.value > x:

            if not self.left:
                self.left = BstNode(x)
                return

            self.left.insert(x)
        else:
            if not self.right:
                self.right = BstNode(x)
                return

            self.right.insert(x)

    def _find(self, node, x):
        if node:
            if node.value == x:
                return True

            if node.value < x:
                return self._find(node.right, x)
            else:
                return self._find(node.left, x)

        return False

    def find(self, x):
        return self._find(self, x)


    def inorder_traversal(self):
        _inorder_traversal(self)

    def level_traversal(self):
        _level_traversal(self)



