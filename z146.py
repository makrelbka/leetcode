class LRUCache:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    class Linkedlist:
        def __init__(self):
            self.head = None
            self.tail = None

        def remove(self, node):
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            if node == self.head:
                self.head = node.next
            if node == self.tail:
                self.tail = node.prev
            node.prev = None
            node.next = None

        def add_head(self, node):
            node.next = self.head
            node.prev = None
            if self.head:
                self.head.prev = node
            self.head = node
            if not self.tail:
                self.tail = node

        def remove_tail(self):
            if self.tail:
                tail = self.tail
                self.remove(tail)
                return tail
            return None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.value_map = {}
        self.node_map = {}
        self.list = LRUCache.Linkedlist()

    def get(self, key: int) -> int:
        if key not in self.value_map:
            return -1
        node = self.node_map[key]
        self.list.remove(node)
        self.list.add_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.value_map:
            node = self.node_map[key]
            node.value = value
            self.list.remove(node)
            self.list.add_head(node)
        else:
            if len(self.value_map) >= self.capacity:
                tail = self.list.remove_tail()
                if tail:
                    del self.value_map[tail.key]
                    del self.node_map[tail.key]
            new_node = LRUCache.Node(key, value)
            self.list.add_head(new_node)
            self.value_map[key] = value
            self.node_map[key] = new_node