# File Recursion

## Notes

Test directories can be found [here](https://s3.amazonaws.com/udacity-dsand/testdir.zip)

## Approach

Recursion, using depth first search, since there is no explicit requirements on the order of the traversals

-   By default it will look for all c files under current folder.
-   If folder is not found, it will return empty array instead of throwing errors.
