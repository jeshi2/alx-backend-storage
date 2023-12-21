#!/usr/bin/env python3
""" 8-all """
from pymongo.collection import Collection
from typing import List


def list_all(mongo_collection: Collection) -> List[dict]:
    """
    Lists all documents in a MongoDB collection.

    Returns:
        List[dict]: A list containing all documents in the collection.
    """
    documents = list(mongo_collection.find())
    return documents
