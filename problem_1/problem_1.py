#!/usr/bin/env python3
"""find out the maximum numbers of 'A' you can print on screen
"""
from typing import List


def list_append(data: List, value, instruction: str):
    if instruction == "append":
        data.append(value)
    elif instruction == "replace":
        data[-1] = value[1]
        data[-2] = value[0]
        data.append(value[2])


def max_output(n: int):
    """Algorithm to find max output"""
    char_List = ["A", "Ctrl-A", "Ctrl-C", "Ctrl-V"]
    sequence_List = list()
    v_count = 0
    result_count = 0
    copy_count = 0

    for i in range(n):
        if i < 5:
            result_count += 1
            list_append(sequence_List, char_List[0], "append")

        elif i == 5:
            list_append(sequence_List, char_List[1:], "replace")
            result_count -= 2
            copy_count = result_count
            result_count += copy_count

        if i > 5 and v_count < 3:
            result_count += copy_count
            list_append(sequence_List, char_List[3], "append")
            v_count += 1

        elif i > 5 and v_count == 3:
            v_count = 0
            list_append(sequence_List, char_List[1:], "replace")
            result_count -= (copy_count * 2)
            copy_count = result_count
            result_count += copy_count

    print(result_count, "-> for the sequence: {}".format(sequence_List))


# max_output(50)
