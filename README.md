# dsa_practice

## Maths Formula

Average
`average = sum of n / total length`

Median
Odd median
`(n + 1) / 2`
Even median
`(n/2) + (n/2 + 1) / 2`
where n is the length

Exponent
`a1 * (r^n)`
where,
a1 = first element
r = uniform increasing number
n = length/no of times

Logarithm
A logarithm is the inverse of an exponent.

log216 = 4

"log216" can be read as "log base 2 of 16", and means "the number of times 2 must be multiplied by itself to equal 16".
"log216" might also be written as log2(16)

In python, log is written as ```math.log(16, 2)```

Factorial
`n!` of positive integer only
example: `3! is equal to 3 * 2 * 1` 

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
