#!/usr/bin/env python3
'''Asyncronous Python
'''
from typing import List
import asyncio


time_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Spawns wait_random n times with a specified delay
    between each call.
    Args:
        n: number of times to spawn wait_random
        max_delay: maximum delay between each call
    Returns:
        list of delays
    '''
    res = await asyncio.gather(
        *tuple(map(lambda _: time_wait_random(max_delay), range(n)))
    )
    return sorted(res)
