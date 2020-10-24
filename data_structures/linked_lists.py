class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

        def __repr__(self):
            return f"{{data: {repr(self.data)}}}"

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __eq__(self, other):
        if len(self) != len(other): return False
        return self.to_array() == other.to_array()

    def __repr__(self):
        if self.is_empty(): return "Empty"
        else:
            node_strs = []
            curr_node = self.head
            for curr_index in range(self.size):
                node_strs.append(f"{curr_index} {repr(curr_node)}")
                curr_node = curr_node.next
            return " -> ".join(node_strs)

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

    def insert(self, index, data):
        assert(index >= 0 and index <= len(self))
        node = self.Node(data)
        # Case 0 - No head exists
        if self.is_empty():
            self.head = node
            self.tail = node
        # Case 1 - Add to start
        elif index == 0:
            self.head, node.next = node, self.head
        # Case 2 - Add to tail
        elif index == len(self):
            self.tail.next, self.tail = node, node
        # Case 3 - Insertion in between elements
        else:
            prev = self.head
            for _ in range(index-1):
                prev = prev.next
            prev.next, node.next = node, prev.next
        self.size += 1

    def insert_head(self, data):
        self.insert(0, data)
    
    def insert_tail(self, data):
        self.insert(self.size, data)

    def remove(self, index):
        assert(not self.is_empty())
        assert(index >= 0 and index < len(self))
        # Case 0 - Only one element
        if len(self) == 1:
            out = self.head.data
            self.head = self.tail = None
        # Case 1 - Removing head
        elif index == 0:
            out = self.head.data
            self.head = self.head.next
        # Case 2 - Removing tail
        elif index == len(self)-1:
            out = self.tail.data
            prev = self.head
            for _ in range(index-1):
                prev = prev.next
            self.tail, prev.next = prev, None
        # Case 3 - Removal in between elements
        else:
            prev = self.head
            for _ in range(index-1):
                prev = prev.next
            out = prev.next.data
            prev.next = prev.next.next
        self.size -= 1
        return out

    def remove_head(self):
        return self.remove(0)

    def remove_tail(self):
        return self.remove(len(self)-1)

    def peek(self, index):
        assert(not self.is_empty())
        assert(index >= 0 and index < len(self))
        if index == len(self)-1:
            return self.tail.data
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.data

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