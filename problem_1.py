class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        pass


our_cache = LRU_Cache(1)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.get(1)  # returns -1
our_cache.get(2)  # returns 2
our_cache.get(3)  # returns -1
