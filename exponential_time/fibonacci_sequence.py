 # Fibonacci Sequence in polynomial time
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1

    grandparent, parent = 0, 1
    current = 0  

    for _ in range(n - 1):
        current = parent + grandparent
        grandparent, parent = parent, current
    return current