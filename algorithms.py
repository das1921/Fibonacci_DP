"""
# This code has been created by Diego Salas Polar,
# Johan Arcenal, John Shuford, & Trae White
#
# This file contains the following algorithm(s)
#     rc_fibonacci(term_index)
#     dp_fibonacci(term_index)

# NOTE: 'n' must be greater than or equal to 0
"""


# Recursion Fibonacci Algorithm
def rc_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return rc_fibonacci(n - 1) + rc_fibonacci(n - 2)


# Dynamic Programming Fibonacci Algorithm
def dp_fibonacci(n):
    if n == 0:
        return 0

    prev = 0
    current = i = 1

    while i < n:
        # "nxt" is short for next
        nxt = prev + current
        prev = current
        current = nxt
        i += 1

    return current

