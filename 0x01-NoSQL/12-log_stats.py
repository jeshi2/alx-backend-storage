#!/usr/bin/env python3
"""
12-log_stats.py
"""
from pymongo import MongoClient

def print_logs_stats(logs_collection):
    """ Total number of documents in the collection """
    total_logs = logs_collection.count_documents({})
    print(f"{total_logs} logs")

    """ Methods statistics """
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f"    method {method}: {count}")

    """Status check statistics """
    status_check_count = logs_collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check_count} status check")