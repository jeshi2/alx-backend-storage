#!/usr/bin/env python3
"""
list student average score
"""

def top_students(mongo_collection: Collection) -> List[dict]:
    """
    Returns all students sorted by average score.
    """
    pipeline = [
        {
            "$project": {
                "_id": 1,
                "name": 1,
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]

    students = list(mongo_collection.aggregate(pipeline))
    return students