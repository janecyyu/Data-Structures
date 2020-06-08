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
my_array = [1, 2, 3, 4, 5, 6]


class Stack:
    def __init__(self):
        self.storage = []
        self.size = len((self.storage))

    def __len__(self):
        return(len((self.storage)))

    def push(self, value):
        self.storage.insert(0, value)
        return self.storage

    def pop(self):
        if len((self.storage)) == 0:
            return None
        else:
            rm_data = self.storage.pop(0)
            return rm_data


arr_stack = Stack()
arr_stack.storage = my_array
print(arr_stack.__len__())
print(arr_stack.push(7))
print(arr_stack.pop())
