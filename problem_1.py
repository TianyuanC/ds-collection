class Node:
    def __init__(self, key, val, pre=None, nxt=None):
        self.val = val
        self.key = key
        self.pre = pre
        self.nxt = nxt


class LRU_Cache(object):

    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.lookup = {}
        self.capacity = capacity

    def get(self, key):
        pass

    def set(self, key, value):
        pass

    def display_cache(self):
        pass


cache = LRU_Cache(2)

cache.set(1, 1)
cache.set(2, 2)
assert cache.get(2) == 2
assert cache.get(1) == 1
cache.set(3, 10)
assert cache.get(2) == -1
assert cache.get(3) == 10
