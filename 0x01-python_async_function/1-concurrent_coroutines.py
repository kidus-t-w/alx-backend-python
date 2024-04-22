#!/usr/bin/env python3
"""
1-concurrent_coroutines.py
"""
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    """
    Returns the delay time
    """
    wait_list: List = []
    sort_list: List = []
    for _ in range(n):
        value = await wait_random(max_delay)
        wait_list.append(value)
    for i in range(len(wait_list)):
        sort_list.append(min(wait_list))
        wait_list.remove(min(wait_list))
    return sort_list
