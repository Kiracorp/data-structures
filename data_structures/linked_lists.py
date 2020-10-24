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
        assert(index >= 0 and index <= self.size)
        node = self.Node(data)
        # Case 0 - No head exists
        if self.is_empty():
            self.head = node
            self.tail = node
        # Case 1 - Add to start
        elif index == 0:
            self.head, node.next = node, self.head
        # Case 2 - Add to tail
        elif index == self.size:
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
        assert(index >= 0 and index < self.size)
        data = None
        # Case 0 - Only one element
        if self.size == 1:
            data = self.head.data
            self.head, self.tail = None, None
        # Case 1 - Removing head
        elif index == 0:
            data, self.head = self.head.data, self.head.next
        # Case 2 - Removing tail
        elif index == self.size-1:
            prev, data = self.head, self.tail.data
            for _ in range(index-1):
                prev = prev.next
            self.tail, prev.next = prev, None
        # Case 3 - Removal in between elements
        else:
            prev = self.head
            for _ in range(index-1):
                prev = prev.next
            prev.next, data = prev.next.next, prev.next.data
        self.size -= 1
        return data

    def remove_head(self):
        return self.remove(0)

    def remove_tail(self):
        return self.remove(self.size-1)

    def peek_head(self):
        if self.is_empty(): return None
        return self.head.data
    
    def peek_tail(self):
        if self.is_empty(): return None
        return self.tail.data

    def peek_all(self):
        if self.is_empty(): return []
        curr, lst = self.head, []
        while curr is not None:
            lst.append(curr.data)
            curr = curr.next
        return lst

    def __len__(self):
        return self.size

    def __repr__(self):
        if self.is_empty(): return "Empty"
        else:
            node_strs = []
            curr_node = self.head
            for curr_index in range(self.size):
                node_strs.append(f"{curr_index} {repr(curr_node)}")
                curr_node = curr_node.next
            return " -> ".join(node_strs)