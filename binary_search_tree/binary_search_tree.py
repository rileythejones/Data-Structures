import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


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

    # Return True if the tree contains the value
    # False if it does not 
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

    
#     def contains(self, target):
#         if self.value is target:
#             print("Check Node")
#             return True 
#         elif self.left:
#             print("Check Left")
#             if self.left.value is target:
#                 print("Check Left Node")
#                 return True
#             elif self.left.contains(target):
#                 print("Call contains on Left Node")
#                 return True
#             elif self.right:
#                 print("Check Right within Left")
#                 if self.right.contains(target):
#                     print("Call contains on Right Node within Left Node")
#                     return True

#         elif self.right:
#             print("Check Right")
#             if self.right.value is target:
#                 print("Check Right Node")
#                 return True
#             elif self.right.contains(target):
#                 print("Call contains on Right Node")
#                 return True
#             elif self.left: 
#                 print("Check Left within Right")
#                 if self.left.contains(target):
#                     print("Call contains on Left Node within Right Node")
#                     return True
#         else:
#             return False 
#             print("Return when not found")
#             return False 


    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
