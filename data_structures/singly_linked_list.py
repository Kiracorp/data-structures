from .abstract_linked_list import LinkedList

class SinglyLinkedList(LinkedList):
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

        def __repr__(self):
            return f"{{data: {repr(self.data)}}}"

    def __repr__(self):
        if self.is_empty(): return "Empty"
        else:
            node_strs = []
            curr_node = self.head
            for curr_index in range(self.size):
                node_strs.append(f"{curr_index} {repr(curr_node)}")
                curr_node = curr_node.next
            return " -> ".join(node_strs)

    def insert(self, index, data):
        assert(index >= 0 and index <= len(self))
        node = self.Node(data)
        # Case 0 - No head exists
        if self.is_empty():
            self.head = self.tail = node
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

    def peek(self, index):
        assert(not self.is_empty())
        assert(index >= 0 and index < len(self))
        if index == len(self)-1:
            return self.tail.data
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.data

    def reverse(self):
        if len(self) < 2: return
        curr, nxt = None, self.head
        self.tail = nxt
        while nxt is not None:
            prev, curr, nxt = curr, nxt, nxt.next
            curr.next = prev
        self.head = curr