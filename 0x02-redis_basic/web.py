#!/usr/bin/env python3
import requests
import redis
from functools import wraps
from typing import Callable


def track_access_count(func: Callable) -> Callable:
    """
    Decorator to track the number of times a URL was accessed
    """
    @wraps(func)
    def wrapper(url: str) -> str:
        access_count_key = f"count:{url}"
        access_count = redis_client.get(access_count_key)
        if access_count is None:
            access_count = 0
        else:
            access_count = int(access_count)

        access_count += 1
        redis_client.set(access_count_key, access_count)

        return func(url)

    return wrapper


def cache_result(expiration: int = 10) -> Callable:
    """
    Decorator to cache the result with an expiration time
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(url: str) -> str:
            result_key = f"result:{url}"
            cached_result = redis_client.get(result_key)
            if cached_result is not None:
                return cached_result.decode('utf-8')

            result = func(url)
            redis_client.setex(result_key, expiration, result)
            return result

        return wrapper

    return decorator


@track_access_count
@cache_result()
def get_page(url: str) -> str:
    """
    Get the HTML content of a particular URL
    """
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    redis_client = redis.Redis()

    slow_url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.com"
    fast_url = "http://www.google.com"

    slow_content = get_page(slow_url)
    print(f"Content of slow URL (cached): {slow_content}")

    fast_content = get_page(fast_url)
    print(f"Content of fast URL (not cached): {fast_content}")

    slow_content_cached = get_page(slow_url)
    print(f"Content of slow URL (from cache): {slow_content_cached}")

    slow_access_count = redis_client.get(f"count:{slow_url}")
    print(f"Access count for slow URL: {slow_access_count}")
