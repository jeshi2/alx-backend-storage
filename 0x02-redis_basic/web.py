#!/usr/bin/env python3
import requests
import redis
from functools import wraps
from typing import Callable


def cache_page(method: Callable) -> Callable:
    """
    Decorator to cache the result of a web page retrieval with 
    an expiration time
    :param method: The method to be decorated
    :return: The decorated method
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        redis_client = redis.Redis()

        # Check if the result is already cached
        cached_result = redis_client.get(f"cache:{url}")
        if cached_result is not None:
            # Increment access count
            redis_client.incr(f"count:{url}")
            return cached_result.decode("utf-8")

        # If not cached, retrieve the result using the original method
        result = method(url)

        # Cache the result with an expiration time of 10 seconds
        redis_client.setex(f"cache:{url}", 10, result)

        # Increment access count
        redis_client.incr(f"count:{url}")

        return result

    return wrapper


@cache_page
def get_page(url: str) -> str:
    """
    Retrieve the HTML content of a particular URL and track access counts
    :param url: The URL to retrieve
    :return: The HTML content of the URL
    """
    response = requests.get(url)
    return response.text


# Example usage
if __name__ == "__main__":
    # Use a slow response URL for testing
    slow_url = "http://slowwly.robertomurray.co.uk/delay/10000/url/https://www.example.com"

    # Call the get_page function, which is decorated with caching behavior
    page_content = get_page(slow_url)
    print(page_content)

    # Check the access count for the slow URL
    access_count = redis.Redis().get(f"count:{slow_url}")
    print(f"Access count for {slow_url}: {int(access_count)}")
