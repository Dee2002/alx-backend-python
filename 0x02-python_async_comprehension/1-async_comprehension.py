#!/usr/bin/env python3
"""
Async Comprehension
"""

from typing import List
from asyncio import run
from random import uniform
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using async comprehensions"""
    return [i async for i in async_generator()]
