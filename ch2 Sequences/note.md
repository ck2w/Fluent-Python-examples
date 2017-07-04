# ch2 Sequences

## built-in sequences

1. sequences types

container sequences: store references

flat sequences: store value

mutable sequences

immutable sequences

2. each item in the tuple holds the data for one field and the position of the item gives its meaning

3. The most visible form of tuple unpacking is parallel assignment; that is, assigning items from an iterable to a tuple of variables

4. evaluate the expression `seq[start:stop:step]`, Python calls `seq.__getitem__(slice(start, stop, step))`

