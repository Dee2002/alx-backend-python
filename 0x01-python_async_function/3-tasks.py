#!/usr/bin/env python3
"""
Module for creating asyncio tasks.
"""

import asyncio
from typing import Task
from 0-basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> Task:
    """
    Create and return an asyncio Task for wait_random coroutine with
    given max_delay.
    """
    return asyncio.create_task(wait_random(max_delay))
