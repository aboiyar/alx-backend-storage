#!/usr/bin/env python3
'''Lists all the documents in a collection.
'''
def list_all(mongo_collection):
    return [doc for doc in mongo_collection.find()]
