import hashlib
import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash=0):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None
        self.prev = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = "{0}:{1}:{2}".format(self.timestamp, self.data, self.previous_hash).encode(
            'utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def is_valid(self):
        if self.calc_hash() != self.hash:
            return False
        if self.prev is not None:
            is_valid = True
            hash_ref = self.previous_hash
            node = self.prev
            while node is not None and is_valid:
                if hash_ref != node.hash or node.hash != node.calc_hash():
                    is_valid = False
                    continue
                hash_ref = node.previous_hash
                node = node.prev
            return is_valid
        return True


class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_next(self, data):
        now = datetime.datetime.utcnow().isoformat()
        if self.head is None:
            block = Block(now, data)
            self.head = block
            self.tail = block
        else:
            block = Block(now, data, self.tail.hash)
            self.tail.next = block
            block.prev = self.tail
            self.tail = block

    def is_valid(self):
        if self.tail is None:
            return True
        return self.tail.is_valid()

    def display(self):
        node = self.head
        while node is not None:
            print("data: {0}".format(node.data))
            print("hash: {0}".format(node.hash))
            print("time: {0}".format(node.timestamp))
            print("valid: {0}".format(node.is_valid()))
            print("===")
            node = node.next


block_chain = BlockChain()

# Trivial empty blockchain is always valid
print(block_chain.is_valid())
# True

block_chain.add_next("test1")
block_chain.add_next("test2")
block_chain.add_next("test3")

# Untempered blockchain is valid
print(block_chain.is_valid())
# True

# Altered blockchain is invalid
block_chain.head.next.timestamp = "1234"
print(block_chain.is_valid())
# False
