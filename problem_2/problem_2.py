#!/usr/bin/env python3
"""the maximum distance between a field and a water tower
for buying the right water pump
"""
from typing import List


def max_power(fields: List, towers: List) -> int:
    """a function that returns the max power needed
    for the list of fields and water towers
    """
    ratio = towers[-1] - fields[0]
    power = ratio / len(towers)

    return int(power)


# fields = [1, 5]
# towers = [10]
# print(max_power(fields, towers))
