from data_structures.singly_linked_list import SinglyLinkedList

class Stack:
    def __init__(self):
        self.ll = SinglyLinkedList()

    def __len__(self):
        return len(self.ll)

    def is_empty(self):
        return self.ll.is_empty()

    def push(self, item):
        self.ll.insert_head(item)

    def pop(self):
        return self.ll.pop_head()

    def peek(self):
        return self.ll.peek_head()