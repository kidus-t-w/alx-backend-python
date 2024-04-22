#!/usr/bin/env python3
"""
4-tasks.py
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay
    """
    wait_list: List[float] = []
    sort_list: List[float] = []
    for i in range(n):
        value = await task_wait_random(max_delay)
        wait_list.append(value)
    for i in range(len(wait_list)):
        sort_list.append(min(wait_list))
        wait_list.remove(min(wait_list))
    return sort_list
