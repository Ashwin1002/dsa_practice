# dsa_practice

## Maths Formula

**Average**
`average = sum of n / total length`

**Median**
Odd median
`(n + 1) / 2`
Even median
`(n/2) + (n/2 + 1) / 2`
where n is the length

**Exponent**
`a1 * (r^n)`
where,
a1 = first element
r = uniform increasing number
n = length/no of times

**Logarithm**
A logarithm is the inverse of an exponent.

log216 = 4

"log216" can be read as "log base 2 of 16", and means "the number of times 2 must be multiplied by itself to equal 16".
"log216" might also be written as log2(16)

In python, log is written as ```math.log(16, 2)```

Factorial
`n!` of positive integer only
example: `3! is equal to 3 * 2 * 1` 

**Fibonacci sequence**

The Fibonacci sequence is a sequence of numbers where each number is the sum of the two numbers before it.

```xn = xn−1 + xn−2```
where,

`xn` is term number "n"
`xn−1` is the previous term `(n−1)`
`xn−2` is the term before that `(n−2)`

## The Big O Chart

```
(1) - constant
O(n) - linear
O(n^2) - squared
O(2^n) - exponential
O(n!) - factorial
```

![Big O Time and Space complexity chart](https://github.com/user-attachments/assets/189a71ef-0d4e-436e-b7dc-4658564150de)

`O(nm)` is very similar to O(n^2), but instead of a single input that we care about, there are two. If n and m increase at the same rate, then O(nm) is effectively the same as O(n^2). However, if n or m increases faster or slower, then it's useful to track their complexity separately.

Dictionary look up by key is a `constant time` algorithm.

Binary serach is `O(log(n))`. The array must be sorted.

| Big-O     | Name          | Description |
|-----------|--------------|-------------|
| O(1)      | Constant     | Best: The algorithm always takes the same amount of time, regardless of how much data there is. Example: Looking up an item in a list by index. |
| O(log n)  | Logarithmic  | Great: Algorithms that remove a percentage of the total steps with each iteration. Very fast, even with large amounts of data. Example: Binary search. |
| O(n)      | Linear       | Good: 100 items, 100 units of work. 200 items, 200 units of work. This is usually the case for a single, non-nested loop. Example: Unsorted array search. |
| O(n log n)| Linearithmic | Okay: This is slightly worse than linear, but not too bad. Example: Mergesort and other "fast" sorting algorithms. |
| O(n²)     | Quadratic    | Slow: The amount of work is the square of the input size. 10 inputs, 100 units of work. 100 Inputs, 10,000 units of work. Example: A nested for loop to find all the ordered pairs in a list. |
| O(n³)     | Cubic        | Slower: If you have 100 items, this does 100³ = 1,000,000 units of work. Example: A triple nested for loop to find all the ordered triples in a list. |
| O(2ⁿ)     | Exponential  | Horrible: We want to avoid this kind of algorithm at all costs. Adding one to the input doubles the amount of steps. Example: Brute-force guessing results of a sequence of n coin flips. |
| O(n!)     | Factorial    | Even More Horrible: The algorithm becomes so slow so fast that it is practically unusable. Example: Generating all the permutations of a list. |

## Algorithms

### Sorting

**Bubble Sort**

Bubble sort repeatedly steps through a slice and compares adjacent elements, swapping them if they are out of order. It continues to loop over the slice until the whole list is completely sorted. 

Space complexity: O(1)
Time complexity: O(n^2) on worst case and O(n) on best case(if the array is already sorted)

**Merge Sort**

Merge sort is a recursive sorting algorithm and it's quite a bit faster than bubble sort. It's a divide and conquer algorithm
-Divide: divide the large problem into smaller problems, and recursively solve the smaller problems
- Conquer: Combine the results of the smaller problems to solve the large problem

Space complexity: O(n) faster for longer list
Time complexity: O(nlog(n))

**Insertion Sort**

Insertion sort builds a sorted list one item at a time. It's much less efficient on large lists than merge sort because it's O(n^2), but it's actually faster (not in Big O terms, but due to smaller constants) than merge sort on small lists.

Space complexity: O(1)
Time complexity: O(n^2) and on O(n) on presorted list

**Quick Sort**

Quick sort is an efficient sorting algorithm that's widely used in production sorting implementations. Like merge sort, quick sort is a recursive divide and conquer algorithm.

Divide:
- Select a pivot element that will preferably end up close to the center of the sorted pack
- Move everything onto the "greater than" or "less than" side of the pivot
- The pivot is now in its final position
- Recursively repeat the operation on both sides of the pivot

Conquer:
- The array is sorted after all elements have been through the pivot operation

While the version of quicksort that we implemented is almost always able to perform at speeds of O(n*log(n)), its Big O is still technically O(n^2) due to the worst-case scenario. We can fix this by altering the algorithm slightly.

Space complexity: O(1)
Time complexity: O(n*log(n)) and on worst case O(n^2)

Quick sort is used default in PostgreSQL.

## Data Structures

Space complexity in a `list` data type:

`Append`: appending to end of a list is `O(1)`
`index`: accessing item through an index is `O(1)`
`delete`: deleting an item from list is `O(n)`
`searching`: searching an item in a list if `O(n)`

**Stack**

A stack is a data structure that stores ordered items. It's like a list, but its design is more restrictive. It only allows items to be added or removed from the top of the stack. It is a LIFO (last in, first out) data structure.

| Operation | Big O | Description |
|-----------|-------|-------------|
| push      | O(1)  | Add an item to the top of the stack |
| pop       | O(1)  | Remove and return the top item from the stack |
| peek      | O(1)  | Return the top item from the stack without modifying the stack |
| size      | O(1)  | Return the number of items in the stack |


**Queue**

A queue is a data structure that stores ordered items. It's like a list, but again, like a stack, its design is more restrictive. A queue only allows items to be added to the tail of the queue and removed from the head of the queue.

| Operation | Big O | Description |
|-----------|-------|-------------|
| push      | O(n)  | Add an item to the back of the queue |
| pop       | O(1)  | Remove and return the front item from the queue |
| peek      | O(1)  | Return the front item from the queue without modifying the queue |
| size      | O(1)  | Return the number of items in the queue |


**Linked List**

A linked list is a linear data structure where elements are not stored next to each other in memory. The elements in a linked list are linked using references to each other. Example, an element of index 3 carries reference of index 2.

The difference is that Items in a "normal" list are stored next to each other in memory, and to get an item from a List we use a numbered index. With a normal list, all the data is stored in the same place in memory and the index is just a way to find the right spot.

In a linked list, there are no indexes. Each node contains the data itself as well as a reference to the next node in the list. Iterating over a linked list requires starting at the head node and following the next references until you reach the end.

Linked List has `O(1)` insertion and deletion but consumes more memory than normal arrays.

**Binary Tree**

One of the most common types of ordered tree is a Binary Search Tree or BST. In addition to the properties we've already talked about, a BST has some additional constraints:

- Instead of an unbounded list of children, each node has at most 2 children
- The left child's value must be less than its parent's value
- The right child's value must be greater than its parent's value
- No two nodes in the BST can have the same value

By ordering the tree this way, we'll be able to add, remove, find, and update nodes much more quickly.

The read, delete, insert or search operation in binary tree for best case is `O(n)` and `O(log n)` for average and worst cases.


**Red-Black Tree**

A red-black tree is a kind of binary search tree that solves the "balancing" problem. It contains a bit of extra logic to ensure that as nodes are inserted and deleted, the tree remains relatively balanced.

Each node in an RB Tree stores an extra bit, called the "color": either red or black. The "color" ensures that the tree remains approximately balanced during insertions and deletions. When the tree is modified, the new tree is rearranged and repainted to restore the coloring properties that constrain how unbalanced the tree can become in the worst case.

**Hashmaps**

A hash map or "hash table" is a data structure that maps keys to values. The lookup, insertion, and deletion operations of a hashmap have an average computational cost of `O(1)`. Hashmaps are built on top of arrays (or in the case of ours, a Python list).

**Tries**

A trie is also often referred to as a "prefix tree" because it can be used to efficiently find all of the words that start with a given prefix.