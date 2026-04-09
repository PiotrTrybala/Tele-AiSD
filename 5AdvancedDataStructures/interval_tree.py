from math import floor
from bst import BstNode

class ListNode:
    def __init__(self, value):
        self.next = None
        self.value = value
        self.bst = BstNode(value + 0.5)

class IntervalTree:

    def __init__(self):
        self.head = ListNode(0.0)

    def insert(self, x):
        lower_bound = floor(x)

        new_node = ListNode(lower_bound)
        new_node.bst.insert(x)

        cur = self.head
        prev = None
        while cur.next and cur.value < x:
            if cur.value == lower_bound:
                break
            prev = cur
            cur = cur.next

        if cur.value == lower_bound:
            cur.bst.insert(x)
            return

        if cur.next:
            successor = cur
            prev.next = new_node
            prev.next.next = successor
        else:
            cur.next = new_node

    def search(self, x):
        lower_bound = floor(x)

        cur = self.head
        while cur.next and cur.value < x:
            if cur.value == lower_bound:
                break
            cur = cur.next

        if not cur.next:
            return False

        return cur.bst.search(x)

    def min(self, y):
        cur = self.head

        while cur.next and y > 0:
            cur = cur.next
            y -= 1

        if not cur.next:
            return -1

        return cur.bst.min()


    def max(self, y):
        cur = self.head

        while cur.next and y > 0:
            cur = cur.next
            y -= 1

        if not cur:
            return -1

        return cur.bst.max()

    def size(self):
        size = 0

        cur = self.head
        while cur.next:
            cur = cur.next
            size += 1

        return size
