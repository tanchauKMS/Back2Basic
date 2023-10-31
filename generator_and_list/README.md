# Python Generator vs List

Python generators and sets are both data structures that can be used to store unique values. However, there are some key differences between the two:

## Generators

- Generators are lazy, meaning that they do not generate all of their values at once. Instead, they generate values one at a time, as needed.
- Generators are memory-efficient, because they only store the state necessary to generate the next value.
- Generators can be used to implement infinite sequences.

## Sets

- Sets are eager, meaning that they generate all of their values at once when they are created.
- Sets are not memory-efficient as generators, because they need to store all of their values in memory.
- Sets cannot be used to implement infinite sequences.

## When to use

### Generator

Generators are useful when you need to iterate over a large sequence of values without storing all of the values in memory. 

```
For example, you could use a generator to iterate over all of the lines in a file, or all of the results of a database query.
```

### Set

Sets are useful when you need to store a unique set of values. 
```
For example, you could use a set to store the unique words in a document, or the unique items in a shopping cart.
```