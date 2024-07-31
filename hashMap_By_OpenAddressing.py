class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class MyHashMap:

    def __init__(self, cap=8, max_threshold=0.75):
        self.cap = cap
        self.size = 0
        self.max_threshold = max_threshold
        self.data = [None] * self.cap
        self.deleted = [False] * self.cap  # Track deleted slots

    def hash_function(self, key):
        return hash(key) % self.cap

    def probe(self, index, key):
        # Linear probing
        start_index = index
        while (self.data[index] is not None and self.data[index].key != key) or self.deleted[index]:
            index = (index + 1) % self.cap
            if index == start_index:
                break
        return index

    def put(self, key: int, value: int) -> None:
        if self.size >= self.cap * self.max_threshold:
            self.resize()
        index = self.hash_function(key)
        probe_index = self.probe(index, key)

        if self.data[probe_index] is None or self.deleted[probe_index]:
            self.data[probe_index] = Entry(key, value)
            self.deleted[probe_index] = False
            self.size += 1
        else:
            self.data[probe_index].value = value

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        probe_index = self.probe(index, key)
        
        if self.data[probe_index] is None:
            return -1
        return self.data[probe_index].value if self.data[probe_index].key == key else -1

    def remove(self, key: int) -> None:
        index = self.hash_function(key)
        probe_index = self.probe(index, key)
        
        if self.data[probe_index] is not None and self.data[probe_index].key == key:
            self.data[probe_index] = None
            self.deleted[probe_index] = True
            self.size -= 1

    def resize(self):
        old_data = self.data
        old_deleted = self.deleted
        self.cap = 2 * self.cap
        self.size = 0
        self.data = [None] * self.cap
        self.deleted = [False] * self.cap

        for i in range(len(old_data)):
            if old_data[i] is not None and not old_deleted[i]:
                self.put(old_data[i].key, old_data[i].value)

# Example usage
hash_map = MyHashMap()

hash_map.put(1, 1)
hash_map.put(2, 2)
print(hash_map.get(1))  # return 1
print(hash_map.get(2))  # return 2
print(hash_map.get(3))  # return -1, since key 3 does not exist
hash_map.remove(2)
print(hash_map.get(2))  # return -1, since key 2 has been removed
