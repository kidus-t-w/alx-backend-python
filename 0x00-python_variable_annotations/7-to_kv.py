#!/usr/bin/env python3
"""
7-to_kv.py
"""
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    t = {k, v**2}
    return t
