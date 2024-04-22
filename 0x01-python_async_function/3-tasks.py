#!/usr/bin/env python3
"""
3-tasks.py
"""
from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Returns tasks
    """
    value = create_task(wait_random(max_delay))

    return value
