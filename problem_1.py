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
        self.count = 0
        self.lookup = {}
        self.capacity = capacity

    def get(self, key):
        result = -1
        if key in self.lookup:
            hit = self.lookup.get(key)
            result = hit.val
            if self.head is not None and key != self.head.key:
                old_head = self.head
                old_head.pre = hit
                if hit.pre is not None:
                    hit.pre.nxt = hit.nxt
                if hit.nxt is not None:
                    hit.nxt.pre = hit.pre
                else:
                    self.tail = hit.pre
                hit.pre = None
                hit.nxt = old_head
                self.head = hit
        return result

    def set(self, key, value):
        node = Node(key, value)
        if self.count < self.capacity:
            self.lookup[key] = node
            self.count += 1
            if self.head is None:
                self.head = node
            else:
                self.tail.nxt = node
                node.pre = self.tail
            self.tail = node
        else:
            tail = self.tail
            if tail is not None:
                self.lookup[key] = node
                del self.lookup[tail.key]
                if tail.pre is not None:
                    tail.pre.nxt = node
                node.pre = tail.pre
                self.tail = node

    def display(self):
        msg = ""
        curr = self.head
        while curr is not None:
            msg += "[{0}: {1}] -> ".format(curr.key, curr.val)
            curr = curr.nxt
        print(msg)


cache = LRU_Cache(0)
cache.set(1, 1)
cache.set(2, 2)
assert cache.get(1) == -1
assert cache.get(2) == -1
assert cache.get(3) == -1

cache = LRU_Cache(1)
cache.set(1, 1)
cache.set(2, 2)
assert cache.get(1) == -1
assert cache.get(2) == 2
assert cache.get(3) == -1

cache = LRU_Cache(3)
cache.set(1, 1)
cache.set(2, 5)
cache.set(7, 9)
assert cache.get(7) == 9
assert cache.get(1) == 1
cache.set(3, 10)
assert cache.get(2) == -1
assert cache.get(3) == 10
