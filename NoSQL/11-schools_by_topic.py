#!/usr/bin/env python3
"""
Where can I learn Python?
"""


def schools_by_topic(mongo_collection, topic):

    """
    a function that returns the list of school having a specific topic:
    """

    value = {"topics": topic}
    return mongo_collection.find(value)
