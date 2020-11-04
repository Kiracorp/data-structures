from data_structures.abstract_linked_list import LinkedList

class DoublyLinkedList(LinkedList):
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

        def __repr__(self):
            return f"{{data: {repr(self.data)}}}"

    def __repr__(self):
        if self.is_empty(): return "Empty"
        else:
            node_strs = []
            curr_node = self.head
            for curr_index in range(self.size):
                if curr_node.next is not None:
                    assert(id(curr_node) == id(curr_node.next.prev))
                node_strs.append(f"{curr_index} {repr(curr_node)}")
                curr_node = curr_node.next
            return " <-> ".join(node_strs)

    def insert(self, index, data):
        assert(index >= 0 and index <= len(self))
        node = self.Node(data)
        # Case 0 - No head exists
        if self.is_empty():
            self.head = self.tail = node
        # Case 1 - Add to start
        elif index == 0:
            self.head.prev, node.next = node, self.head
            self.head = node
        # Case 2 - Add to tail
        elif index == len(self):
            self.tail.next, node.prev = node, self.tail
            self.tail = node
        # Case 3 - Insertion in between elements
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            prev = curr.prev
            prev.next, curr.prev = node, node
            node.prev, node.next = prev, curr
        self.size += 1

    def pop(self, index):
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
            self.head.prev = None
        # Case 2 - Removing tail
        elif index == len(self)-1:
            out = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
        # Case 3 - Removal in between elements
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            out = curr.data
            prev, nxt = curr.prev, curr.next
            prev.next, nxt.prev = nxt, prev
        self.size -= 1
        return out

    def peek(self, index):
        assert(not self.is_empty())
        assert(index >= 0 and index < len(self))
        if index < len(self)//2:
            # Search from head
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            # Search from tail
            curr = self.tail
            for _ in range(self.size-1-index):
                curr = curr.prev
        return curr.data

    def reverse(self):
        if len(self) < 2: return
        curr = self.head
        self.head, self.tail = self.tail, self.head
        while curr is not None:
            curr.next, curr.prev = curr.prev, curr.next
            curr = curr.prev