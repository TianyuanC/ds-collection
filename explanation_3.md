# Huffman Coding

## Encoding

First of all, use a dictionary to generate the frequency table.

And then use min-heap to store all the nodes with frequency count as the key.

During the code generation phase, I used depth first search to extract the code from the huffman tree recursively

### Analysis

Building the frequency table takes `O(n)`, the heap tree construction is also `O(n)` because we are removing the top two nodes and insert one all cost `O(1)` for heap, finally the translation is again `O(n)`,
and thus it's `O(n)` overall

## Decoding

Decoding is performed iteratively, scanning each digit against the huffman tree.

If it's leave node, reset to root node  
Otherwise, go to left or right child based on whether the value is 0 or 1

### Analysis

`O(n)` because we need to scan through all the encoded string
