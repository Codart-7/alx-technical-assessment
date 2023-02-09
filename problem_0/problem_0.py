#!/usr/bin/env python3
"""find x, the first number of teaspoons of sugar
that will make your cake too sweet.
"""
from tooSweet import isTooSweet


def first_number(n):
    """Use recursive algorithm to find x"""
    if isTooSweet(n) is False:
        return round(n, 1)  # return 1 decimal place
    else:
        return (first_number(n - 0.2))  # assume teaspoon caliberation is 0.2
