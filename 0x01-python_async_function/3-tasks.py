#!/usr/bin/env python3
'''Asyncronous Python
'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
        Returns a task that waits for a random number of seconds
    Args:
        max_delay: maximum number of seconds that the task will wait
    Returns: an asyncio.Task object
    '''
    return asyncio.create_task(wait_random(max_delay))
