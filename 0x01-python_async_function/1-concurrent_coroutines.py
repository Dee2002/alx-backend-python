#!/usr/bin/env python3
"""
Module for executing multiple coroutines concurrently.
"""

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Execute wait_random coroutine n times concurrently with specified max_delay.
    Return list of delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*tasks))
