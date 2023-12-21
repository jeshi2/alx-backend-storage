#!/usr/bin/env python3
""" list all document in mongodb """


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Returns:
        List[dict]: A list containing all documents in the collection.
    """
    return mongo_collection.find()
