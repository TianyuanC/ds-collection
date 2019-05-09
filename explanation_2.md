# File Recursion

## Notes

Test directories can be found [here](https://s3.amazonaws.com/udacity-dsand/testdir.zip)

## Approach

Recursion, using depth first search, since there is no explicit requirements on the order of the traversals

-   By default it will look for all c files under current folder.
-   If folder is not found, it will return empty array instead of throwing errors.

## Analysis

The DFS is going through all files and folders, thus, `O(m+n)` where m and n represents all folders and files respectively
