#!/usr/bin/env python3
"""
Async Comprehensions
"""
import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Run time for four parallel comprehensions"""

    start = time.time()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    return (time.time() - start)
