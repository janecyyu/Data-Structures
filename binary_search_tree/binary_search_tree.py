"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # 1. if no root
        if self is None:
            # if isn't, create the node and park it there
            self = BSTNode(value)
        # 2. there is a root
        else:
            # comparer the value
            if value < self.value:
                # go left
                # if another node on this side
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = BSTNode(value)

            else:
                # else go right
                # Return True if the tree contains the value
                # False if it does not
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = BSTNode(value)

    def contains(self, target):
        # if no root, return none
        if self is None:
            return None
        # if root equals target, return true
        elif self.value == target:
            return True
        else:
            # if target greater than self's value, go right
            if target > self.value:
                if self.right:
                    # repeat again the previous steps
                    self.right.contains(target)
                # if no more elements means not found
                else:
                    return False
            # if target less than self's value, go left
            if target < self.value:
                if self.left:
                    # repeat again the previous steps
                    self.left.contains(target)
                # if no more elements means not found
                else:
                    return False

    def get_max(self):

        # if no root, return none:
        if self is None:
            return None

        max_so_far = self.value
        # if left side or right side no elements, return max_so_far
        if self.right is None or self.left is None:
            return max_so_far

        left_max = self.left.get_max()
        right_max = self.right.get_max()
        # if left value greater than max_so_far, update max_so_far
        if max_so_far < left_max:
            max_so_far = left_max

        # if right value greater than max_so_far, update max_so_far
        if max_so_far < right_max:
            max_so_far = right_max

        return max_so_far

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # if empty return none
        if self is None:
            return
        self.left.for_each(fn)
        self.right.for_each(fn)

    # Part 2 -----------------------

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

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
