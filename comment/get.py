import json
import os
import pymongo
from mode import *

# Connection String
client = pymongo.MongoClient(mongosettings[URL])
db = client[mongosettings[MONGODB]]
collection = db[mongosettings[COMMENTSCOLLECTION]]


def get(event, context):
    command_items = event['pathParameters']['command']
    try:
        topic = command_items
        comments = list(collection.find({'topic':topic}))
        comments.reverse()

        response = {
            "statusCode": 200,
            "body": json.dumps(comments)
        }
    except Exception as e: 
        response = {
            "statusCode": 400,
            "body": str(e),
        }

    return response
    
