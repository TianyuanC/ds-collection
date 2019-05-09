from collections import defaultdict


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    pool = set()
    result = LinkedList()
    if llist_1.head is None:
        ptr = llist_2.head
    else:
        llist_1.tail.next = llist_2.head
        ptr = llist_1.head

    while ptr:
        val = ptr.value
        if val not in pool:
            pool.add(val)
            result.append(val)
        ptr = ptr.next
    if llist_1.tail is not None:
        llist_1.tail.next = None
    return result


def intersection(llist_1, llist_2):
    result = LinkedList()
    if llist_1.head is None:
        return result
    pool_1 = set()

    ptr = llist_1.head
    while ptr:
        val = ptr.value
        if val not in pool_1:
            pool_1.add(val)
        ptr = ptr.next

    pool_2 = set()
    ptr = llist_2.head
    while ptr:
        val = ptr.value
        if val in pool_1 and val not in pool_2:
            pool_2.add(val)
            result.append(val)
        ptr = ptr.next

    return result


def test_case(element_1, element_2):
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))


# Test case 1
# empty linked list merge/intersect shouldn't fail
element_1 = []
element_2 = []
test_case(element_1, element_2)
#
#

# Test case 2
# interset on empty linked list should return nothing
element_1 = []
element_2 = [2, 1, 2]
test_case(element_1, element_2)
# 2 -> 1 ->
#

# Test case 3
# normal test case with duplicates
element_1 = [1, 1, 2, 3, 7]
element_2 = [5, 5, 3, 9]
test_case(element_1, element_2)
# 1 -> 2 -> 3 -> 7 -> 5 -> 9 ->
# 3 ->
