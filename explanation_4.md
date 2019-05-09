# Active Directory

## Approach

Depth first search won't scale because it might cause stack overflow due to nested recursion calls.

So I picked breadth first search, using a stack to keep track of the groups needs to be checked, and add more to it when a group contains subgroups

## Analysis

The BFS algorithm scan through all the groups and their users, so the worst case will be `O(m+n)`, where m and n stands for all groups and users in total
