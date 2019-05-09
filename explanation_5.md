# Blockchain

## Approach

Implemented doubly linked list so it will be easier to implement the chain extending as well as the chain validation

## Analysis

`add` blocks is computed based on the previous hash and current data and timestamp, so it's `O(1)`

`validate` needs to trace all the way up to the root to make sure the intermediate nodes are not altered, and thus `O(n)`
