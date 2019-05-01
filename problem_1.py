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
        # [key: node] lookup
        self.lookup = {}
        self.capacity = capacity

    def get(self, key):
        """
        Retrieve LRU cache value based on the key

        Args:
        key(str): cache key

        Returns:
        -1 if cache miss, otherwise, returns cached value
        """
        result = -1
        if key in self.lookup:
            hit = self.lookup.get(key)
            result = hit.val
            if self.head is not None and key != self.head.key:
                # head -> a -> ... -> hit
                # hit -> head -> a -> ...
                old_head = self.head
                old_head.pre = hit

                # ... -> a -> hit -> b
                # hit -> ... -> a -> b
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
        """
        Sets LRU cache key and value

        Args:
        key(str): cache key
        value(str): cache value
        """
        # value replacement
        if key in self.lookup:
            self.lookup[key].val = value
            return

        node = Node(key, value)
        # a -> b
        # a -> b -> node
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
            # a -> b
            # a -> node
            if tail is not None:
                self.lookup[key] = node
                del self.lookup[tail.key]
                if tail.pre is not None:
                    tail.pre.nxt = node
                node.pre = tail.pre
                self.tail = node

    def display(self):
        """
        Prints out the internal linked list
        e.g.,
        [1: 2] -> [2: 8] -> end

        """
        msg = ""
        curr = self.head
        while curr is not None:
            msg += "[{0}: {1}] -> ".format(curr.key, curr.val)
            curr = curr.nxt
        msg += "end"
        print(msg)


# trivial no cache, all retrivals will be miss
cache = LRU_Cache(0)
cache.set(1, 1)
cache.set(2, 2)
print(cache.get(1))
# -1
print(cache.get(1))
# -1
print(cache.get(1))
# -1


# single cache capacity, set and replace
print()
cache = LRU_Cache(1)
cache.set(1, 1)
cache.set(2, 2)
cache.set(2, 4)
print(cache.get(1))
# -1
print(cache.get(2))
# 4
print(cache.get(3))
# -1

# normal LRU scenario
print()
cache = LRU_Cache(3)
cache.set(1, 1)
cache.set(2, 5)
cache.set(7, 9)
print(cache.get(7))
# 9
print(cache.get(1))
# 1
cache.set(3, 10)
print(cache.get(2))
# -1
print(cache.get(3))
# 10
