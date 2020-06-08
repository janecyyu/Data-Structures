"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""

# Array version:


# class Stack:
#     def __init__(self):
#         self.storage = []
#         self.size = len((self.storage))

#     def __len__(self):
#         return(len((self.storage)))

#     def push(self, value):
#         self.storage.insert(0, value)
#         return self.storage

#     def pop(self):
#         if len((self.storage)) == 0:
#             return None
#         else:
#             rm_data = self.storage.pop(0)
#             return rm_data

# Linked List version:
from singly_linked_list import LinkedList


class Stack:
    def __init__(self):
        self.storage = LinkedList()
        self.size = self.storage.getCount()

    def __len__(self):
        return(self.storage.getCount())

    def push(self, value):
        self.storage.add_to_tail(value)
        return self.storage

    def pop(self):
        if self.storage.getCount() == 0:
            return None
        else:
            rm_data = self.storage.remove_tail()
            return rm_data
