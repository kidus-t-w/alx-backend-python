#!/usr/bin/env python3
"""
6-sum_mixed_list.py
"""
from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """
    Returns the sum of a float and int

    Args:
        mxd_lst (List): List of integer and float to be added
    """
    return float(sum(mxd_lst))
