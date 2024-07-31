class Entry:
    def __init__(self, key, value, hash):
        self.key = key
        self.value = value
        self.hash = hash

class MyHashMap:

    def __init__(self, cap=8, size=0, max_threshold=0.75):
        self.cap = cap
        self.size = size
        self.max_threshold = max_threshold
        self.data = [[] for _ in range(self.cap)]

    def put(self, key: int, value: int) -> None:
        if self.size >= self.cap * self.max_threshold:
            self.resize()
        e = Entry(key, value, hash(key) % self.cap)
        isPresent = False

        for i in range(len(self.data[e.hash])):
            if self.data[e.hash][i].key == key:
                self.data[e.hash][i] = e
                isPresent = True
                break

        if not isPresent:
            self.data[e.hash].append(e)
            self.size += 1

    def get(self, key: int) -> int:
        idx = hash(key) % self.cap
        for elm in self.data[idx]:
            if elm.key == key:
                return elm.value
        return -1

    def remove(self, key: int) -> None:
        idx = hash(key) % self.cap
        for elm in self.data[idx]:
            if elm.key == key:
                self.data[idx].remove(elm)
                self.size -= 1
                break

    def resize(self):
        new_cap = 2 * self.cap
        new_data = [[] for _ in range(new_cap)]
        for i in range(self.cap):
            for elm in self.data[i]:
                new_hash = hash(elm.key) % new_cap
                new_data[new_hash].append(Entry(elm.key, elm.value, new_hash))
        self.cap = new_cap
        self.data = new_data


hash_map = MyHashMap()

hash_map.put(1, 1)
hash_map.put(2, 2)
print(hash_map.get(1))  # return 1
print(hash_map.get(2))  # return 2
print(hash_map.get(3))  # return -1, since key 3 does not exist
hash_map.remove(2)
print(hash_map.get(2))  # return -1, since key 2 has been removed