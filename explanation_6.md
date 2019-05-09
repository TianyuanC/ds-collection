# Linked List Union and Intersection

## Union

### Approach

Chain the two linked list together by introducing `tail` in the linked list.

Removing duplicates by using the `set`

### Analysis

Assume the `set` has a perfect hash function, which means the time complexity for set lookup is O(1)

The overall union operation will be O(m+n) where m, n is the size of the two linked lists respectively

## Intersection

### Approach

Scan through the first linked list and record non-duplicate values by using `set`

Only include the result if it's already in the above set and haven't added to the result yet.

### Analysis

We are iterating through the elements in each of the linked list once.

O(max(m, n)), where m, n is the size of the two linked lists respectively
