# from math import floor
#
# class BstNode:
#
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#     def insert(self, x):
#
#         if self.value > x:
#
#             if not self.left:
#                 self.left = BstNode(x)
#                 return
#
#             self.left.insert(x)
#         else:
#             if not self.right:
#                 self.right = BstNode(x)
#                 return
#
#             self.right.insert(x)
#
#     def _find(self, node, x):
#         if node:
#             if node.value == x:
#                 return True
#
#             if node.value < x:
#                 return self._find(node.right, x)
#             else:
#                 return self._find(node.left, x)
#
#         return False
#
#     def find(self, x):
#         return self._find(self, x)
#
#     def min(self):
#         cur = self
#         while cur.left:
#             cur = cur.left
#
#         return cur.value
#
#     def max(self):
#         cur = self.right
#         while cur.right:
#             cur = cur.right
#
#         return cur.value
#
#
#     def _print(self, node, level=0, _left=True, prefix="", indent=""):
#
#         dashes = '-' * level
#
#         # print(f'value = {node.value}, prefix={prefix}')
#
#         prefix = f'{prefix}{dashes}{node.value}'
#
#         print(indent, end='')
#         print('-' * level, end='')
#         print(node.value, end='')
#
#         if node.left:
#             indent = ''
#             node.left._print(node.left, level + 1, prefix=prefix, indent=indent)
#         else:
#             print()
#
#         if node.right:
#             indent = ' ' * len(prefix)
#             node.right._print(node.right, level + 1, _left = False, prefix=prefix, indent=indent)
#
#     def print(self):
#         self._print(self)
#
# class ListNode:
#     def __init__(self, value):
#         self.next: ListNode | None = None
#         self.value: float = value
#         self.bst: BstNode = BstNode(value + 0.5)
#
#
# class LinkedList:
#
#     def __init__(self):
#         self.head = ListNode(0.0)
#
#     def insert(self, x):
#         limit = floor(x)
#
#         new_node = ListNode(limit)
#         new_node.bst.insert(x)
#
#         cur = self.head
#         prev = None
#         while cur.next and cur.value < x:
#             if cur.value == limit:
#                 break
#             prev = cur
#             cur = cur.next
#         if cur.value == limit:
#             cur.bst.insert(x)
#             return
#
#         if cur.next:
#             successor = cur
#             prev.next = new_node
#             prev.next.next = successor
#         else:
#             cur.next = new_node
#
#
#     def min(self, y):
#
#         limit = floor(y)
#         cur = self.head
#         while cur.next and limit > 0:
#             cur = cur.next
#             limit -= 1
#
#         if not cur:
#             return -1
#
#         return cur.bst.min()
#
#
#
#     def max(self, y):
#         limit = floor(y)
#         cur = self.head
#         while cur.next and limit > 0:
#             cur = cur.next
#             limit -= 1
#
#         if not cur:
#             return -1
#
#         return cur.bst.max()
#
#     def search(self, x):
#         limit = floor(x)
#         cur = self.head
#         while cur.next and cur.value < x:
#             if cur.value == limit:
#                 break
#             cur = cur.next
#
#         if not cur:
#             return False
#
#         return cur.bst.find(x)
#
#     def print(self):
#         cur = self.head
#         while cur.next:
#             cur.bst.print()
#             cur = cur.next
#
# l = LinkedList()
#
# l.insert(1.3)
# l.insert(9.3)
# l.insert(1.6)
# l.insert(4.99)
# l.insert(7.8)
# l.insert(3.7)
# l.insert(4.0)
# l.insert(4.99)
# l.insert(5.01)
# l.insert(7.9)
# l.insert(7.7)
# l.insert(7.6)
# l.insert(7.3)
#
# l.print()
#
# print(f'found 7.7: {l.search(7.7)}')
# print(f'found 100.0: {l.search(100.0)}')
# print(f'min: {l.min(2)}')
# print(f'max: {l.max(2)}')
