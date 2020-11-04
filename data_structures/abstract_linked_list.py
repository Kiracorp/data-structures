from abc import ABC, abstractmethod

class LinkedList(ABC):
    @abstractmethod
    def insert(self, index, data): pass # pragma: no cover

    @abstractmethod
    def pop(self, index): pass # pragma: no cover
        
    @abstractmethod
    def peek(self, index): pass # pragma: no cover
        
    @abstractmethod
    def reverse(self): pass # pragma: no cover

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __eq__(self, other):
        if len(self) != len(other): return False
        return self.to_array() == other.to_array()

    def is_empty(self):
        return self.size == 0 and self.head is None and self.tail is None

    def index_of(self, data):
        curr, i = self.head, 0
        while curr is not None:
            if curr.data == data:
                return i
            curr = curr.next
            i += 1
        return -1

    def insert_head(self, data):
        self.insert(0, data)
    
    def insert_tail(self, data):
        self.insert(self.size, data)
        
    def pop_head(self):
        return self.pop(0)

    def pop_tail(self):
        return self.pop(len(self)-1)

    def peek_head(self):
        return self.peek(0)
    
    def peek_tail(self):
        return self.peek(len(self)-1)

    def to_array(self):
        if self.is_empty(): return []
        curr, lst = self.head, []
        while curr is not None:
            lst.append(curr.data)
            curr = curr.next
        return lst