#!/usr/bin/env python3
"""
Cache module
"""
import uuid
import redis
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of calls to a method
    :param method: The method to be decorated
    :return: The decorated method
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a function
    :param method: The method to be decorated
    :return: The decorated method
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs_key = "{}:inputs".format(method.__qualname__)
        outputs_key = "{}:outputs".format(method.__qualname__)

        # Append input arguments to the inputs list
        self._redis.rpush(inputs_key, str(args))

        # Execute the wrapped function to retrieve the output
        output = method(self, *args, **kwargs)

        # Store the output in the outputs list
        self._redis.rpush(outputs_key, output)

        return output

    return wrapper


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

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis using a randomly generated key
        :param data: The data to be stored in Redis
        :return: The randomly generated key used for storage
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]
            = None) -> Union[str, bytes, int, None]:
        """
        Retrieve data from Redis using the provided key and apply
        the optional conversion function
        :param key: The key used to retrieve data from Redis
        :param fn: Optional callable to convert the retrieved data
        :return: The retrieved data, optionally converted by the
        provided callable
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieve string data from Redis using the provided key
        :param key: The key used to retrieve data from Redis
        :return: The retrieved string data
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieve integer data from Redis using the provided key
        :param key: The key used to retrieve data from Redis
        :return: The retrieved integer data
        """
        return self.get(key, fn=int)
