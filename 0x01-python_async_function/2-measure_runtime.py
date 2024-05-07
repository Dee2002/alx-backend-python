#!/usr/bin/env python3
"""
Module for measuring the runtime of concurrent coroutines.
"""

import asyncio
import time
from typing import Callable


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay) and return average time per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
