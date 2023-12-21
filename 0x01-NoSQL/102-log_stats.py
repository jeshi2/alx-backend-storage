#!/usr/bin/env python3
"""
Log Stats
"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_collection = client.logs.nginx

    """ Total number of logs """
    total_logs = logs_collection.count_documents({})

    print(f"{total_logs} logs")

    """Count of each HTTP method"""
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in http_methods:
        count = logs_collection.count_documents({"method": method})
        print(f"method {method}: {count}")

    """Count of status checks"""
    status_checks = logs_collection.count_documents({"path": "/status"})
    print(f"{status_checks} status check")

    """Top 10 most present IPs"""
    top_ips_pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]

    top_ips_result = logs_collection.aggregate(top_ips_pipeline)

    print("IPs:")
    for ip_entry in top_ips_result:
        ip = ip_entry["_id"]
        count = ip_entry["count"]
        print(f"    {ip}: {count}")