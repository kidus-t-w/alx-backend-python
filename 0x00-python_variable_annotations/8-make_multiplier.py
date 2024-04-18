#!/usr/bin/env python3
"""
8-make_multiplier.py
"""


def make_multiplier(multiplier: float) -> function:
    """
    Returns a function to be multiplied

    Args:
        a (float): float to be multiplied.
    """
    def mul(a: float) -> float:
        return a * multiplier
    return multiplier
