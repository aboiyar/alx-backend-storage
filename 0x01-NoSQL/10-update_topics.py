#!/usr/bin/env python3
'''Update all documents of a collection based on the name.
'''
def update_topics(mongo_collection, name, topics):
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )
