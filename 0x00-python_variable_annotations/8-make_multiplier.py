#!/usr/bin/env python3
"""
8-make_multiplier.py
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function to be multiplied

    Args:
        a (float): float to be multiplied.
    """
    return lambda x: x * multiplier
