import sys
from heapq import *
from collections import defaultdict


class Node:
    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value

    def __lt__(self, other):
        pass


class Code:
    def __init__(self, tree):
        self._codes = {}
        self.tree = tree
        self._generate_code("", self.tree)

    def _generate_code(self, pre, node):
        if node.value != None:
            self._codes[node.value] = pre
        else:
            self._generate_code(pre+"0", node.left)
            self._generate_code(pre+"1", node.right)

    def encode(self, txt):
        encoded = ""
        for char in txt:
            encoded += self._codes[char]
        return encoded


def huffman_encoding(data):
    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1
    heap = []
    for key, value in frequency.items():
        node = Node(None, None, key)
        heappush(heap, (value, node))

    while len(heap) > 1:
        freq_1, node_1 = heappop(heap)
        freq_2, node_2 = heappop(heap)
        root = Node(node_1, node_2)
        heappush(heap, (freq_1 + freq_2, root))

    freq, root = heappop(heap)
    codes = Code(root)

    return codes.encode(data), root


def huffman_decoding(data, tree):
    decoded = ""
    node = tree
    for bit in data:
        if bit == "0":
            node = node.left
        else:
            node = node.right
        if node.value is None:
            continue
        else:
            decoded += node.value
            node = tree

    return decoded


if __name__ == "__main__":
    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))
