#!/usr/bin/env python3
"""
5-sum_list.py
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of floats in a list

    Args:
        input_list (list): list of floats to be added
    """

    sum = 0
    for x in input_list:
        sum += x

    return sum
