#!/usr/bin/env python3
"""
Async Generator
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yield 10 random numbers between 0 and 10 with 1 second interval"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
