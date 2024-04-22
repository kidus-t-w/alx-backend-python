#!/usr/bin/env python3
"""
1-concurrent_coroutines.py
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    wait_list = []
    sort_list = []
    for i in range(n):
        value = await wait_random(max_delay)
        wait_list.append(value)
    for i in range(len(wait_list)):
        sort_list.append(min(wait_list))
        wait_list.remove(min(wait_list))
    return sort_list
