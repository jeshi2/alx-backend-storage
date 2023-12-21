#!/usr/bin/env python3
""" insert document from mongodb """

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB collection based on kwargs.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id