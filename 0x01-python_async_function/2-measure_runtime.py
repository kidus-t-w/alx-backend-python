#!/usr/bin/env python3
"""
2-measure_runtime.py
"""
import time
import asyncio

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n, max_delay):
    """
    Computes the average runtime of  wait_n
    Returns the average time for the computed runtime
    Args:
       n (int): number or times for wait_n to run
       max_delay (int): The maximum amount of delay second
    """
    start_time = time.time()

    asyncio.run(wait_n(n, max_delay))

    return (time.time() - start_time) / n
