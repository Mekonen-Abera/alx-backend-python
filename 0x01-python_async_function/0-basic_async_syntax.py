#!/usr/bin/env python3
'''Python - Async
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
        Returns a random float between 0 and max_delay
    Args:
        max_delay: The maximum delay to return
    Returns:
        A random float between 0 and max_delay
    '''
    wait = random.random() * max_delay
    await asyncio.sleep(wait)
    return (wait)
