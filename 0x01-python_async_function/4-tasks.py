#!/usr/bin/env python3
"""
Module for creating asyncio tasks for multiple coroutines.
"""

import asyncio
from typing import List, Task
from 0-basic_async_syntax import wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Create and execute asyncio tasks for wait_random coroutine n times with specified max_delay.
    Return list of delays.
    """
    tasks: List[Task] = []
    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    return [await task for task in tasks]
