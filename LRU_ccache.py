class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)  
        self.tail = Node(0, 0)  
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add(self, node: Node):
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node
    
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1
    
    def put(self, key: int, value: int):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            node.value = value
            self._add(node)
        else:
            if len(self.cache) >= self.capacity:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
            
            new_node = Node(key, value)
            self._add(new_node)
            self.cache[key] = new_node


lru_cache = LRUCache(2)
lru_cache.put(1, 1)
lru_cache.put(2, 2)
print(lru_cache.get(1)) 
lru_cache.put(3, 3)     
print(lru_cache.get(2)) 
lru_cache.put(4, 4)     
print(lru_cache.get(1))  
print(lru_cache.get(3))  
print(lru_cache.get(4))  
