#!/usr/bin/env python3
"""
7-to_kv.py
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:

    """
        Returns a tuple with a string and a float

        Args:
            k (str): First element of the tuple
            v (float or int): Seconde element to be squared
    """
    return (k, float(v**2))
