import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack
from collections import deque

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:

            if self.left:
                self.left.insert(value)
            else: 
                self.left = BinarySearchTree(value)

        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    def contains(self, target):
        if self.value is target:
            return True
        elif self.value < target:
            if self.right is None:
                return False
            else:
                return BinarySearchTree.contains(self.right, target)
        else:
            if self.left is None:
                return False
            else:
                return BinarySearchTree.contains(self.left, target) 

    def get_max(self):
        node = self
        while node.right:
            node = node.right
        return node.value

    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    def iterative_for_each(self, cb):
        stack = []

        stack.append(self)
        while len(stack) > 0:
            current_node = stack.pop()
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            cb(current_node.value)

    def breadth_first_iterative_for_each(self, cb):
        # depth-first : stack
        # breadth-first: queue

        q = deque()
        q.append(self)

        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            cb(current_node.value)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            node.left.for_each(print)
        print(node.value)
        if node.right:
            node.right.for_each(print)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        node.breadth_first_iterative_for_each(print)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        node.iterative_for_each(print)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
