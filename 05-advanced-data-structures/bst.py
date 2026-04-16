
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

    def search(self, x):
        if self.value == x:
            return True

        if self.value > x:
            if self.left:
                return self.left.search(x)
        else:
            if self.right:
                return self.right.search(x)

        return False

    def min(self):
        cur = self
        while cur.left:
            cur = cur.left
        return cur.value

    def max(self):
        cur = self
        while cur.right:
            cur = cur.right
        return cur.value

    def print(self, level=0, prefix="", indent=""):
       dashes = '-' * level
       prefix = f'{prefix}{dashes}{self.value}'

       print(indent, end='')
       print(dashes, end='')
       print(self.value, end='')

       if self.left:
            indent = ""
            self.left.print(level + 1, prefix, indent)
       else:
           print()

       if self.right:
           indent = ' ' * len(prefix)
           self.right.print(level + 1, prefix, indent)

