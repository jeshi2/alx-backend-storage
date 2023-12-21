#!/usr/bin/env python3
""" list school with topics """
from pymongo.collection import Collection
from typing import List

def schools_by_topic(mongo_collection: Collection, topic: str) -> List[dict]:
    """
    Returns the list of schools having a specific topic.
    """
    filter_query = {'topics': topic}
    schools = list(mongo_collection.find(filter_query))
    return schools