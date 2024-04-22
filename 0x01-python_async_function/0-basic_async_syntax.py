#!/usr/bin/env python3
"""
0-basic_async_syntax.py
"""
import random
import asyncio


async def wait_random(max_delay = 10):
    """
    Waits for a random delay between 0 and max_delay
    Returns random delay 
    Args
        max_delay (int): max delay second
    """
    random_number = random.uniform(0, max_delay)
    
    await asyncio.sleep(random_number)
    return random_number
