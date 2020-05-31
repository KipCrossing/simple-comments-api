import json
import os
import pymongo
from mode import *

# Connection String
client = pymongo.MongoClient(mongosettings[URL])
db = client[mongosettings[MONGODB]]
collection = db[mongosettings[COMMENTSCOLLECTION]]


def get(event, context):
    command_items = event['pathParameters']['command'].split("-")

    if len(command_items) == 1:
        topic = command_items[0]
        # comments = list(collection.find({'topic':topic}))
        comments = list(collection.find({"number": {"$lt": 5, "$gt": 0}, 'topic':topic}))
        comments.reverse()
        # print(comments)
        body = {
            "next": "r1234-20-30",
            "comments": comments,
        }
    elif len(command_items) == 3:
        topic = command_items[0]
        min_range = command_items[1]
        max_range = command_items[2]
        comments = list(collection.find({"number": {"$lt": max_range, "$gt":min_range}, 'topic':topic}))
        body = {
            "next": "r1234-20-30",
            "comments": comments,
        }
    # ballot = collection.find_one({"_id": ballotspec_id})

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    # return response
    return response
