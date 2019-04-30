# LRU cache

## Approach

-   Use Dictionary/HashMap to achieve O(1) of node lookup
-   Use double linked list so that we can make the node swapping O(1)

## Operations

### get

-   cache miss, return -1
-   cache hit, return value and also reorder nodes by moving the hit node to the front, update dictionary

### set

-   under capacity, append to the tail, update dictionary
-   exceed capacity, replace with the tail, update the dictionary
