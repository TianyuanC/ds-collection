# Huffman Coding

## Encoding

First of all, use a dictionary to generate the frequency table.

And then use min-heap to store all the nodes with frequency count as the key.

During the code generation phase, I used depth first search to extract the code from the huffman tree recursively

## Decoding

Decoding is performed iteratively, scanning each digit against the huffman tree.

If it's leave node, reset to root node  
Otherwise, go to left or right child based on whether the value is 0 or 1
