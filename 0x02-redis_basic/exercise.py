#!/usr/bin/env python3
"""
Cache module
"""
import uuid
import redis
from typing import Union

class Cache:
    """
    Cache class for storing data in Redis
    """

    def __init__(self):
        """
        Initialize the Cache instance and flush the Redis database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a randomly generated key
        :param data: The data to be stored in Redis
        :return: The randomly generated key used for storage
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
