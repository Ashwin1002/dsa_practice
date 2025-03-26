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

