#!/usr/bin/python3
"""Minimum number of operations."""


def minOperations(n):
    """Calculate the minimum number of operations to get n 'H' chars."""
    if n < 2:
        return 0
    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
