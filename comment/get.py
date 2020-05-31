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
        num_comments = collection.find({'topic': topic}).count()

        # comments = list(collection.find({'topic':topic}))
        comments = list(collection.find({'topic':topic}))
        comments.reverse()

        response = {
            "statusCode": 200,
            "body": json.dumps(comments)
        }
    else: 
        response = {
            "statusCode": 400,
            "body": str("Bad command"),
        }
        
    return response
    # elif len(command_items) == 3:
    #     topic = command_items[0]
    #     num_comments = collection.find({'topic': topic}).count()
    #     min_range = int(command_items[1])
    #     max_range = int(command_items[2])
    #     if min_range < 1:
    #         min_range = 1
    #     print(min_range)
    #     comments = list(collection.find({"number": {"$lt": max_range + 1, "$gt":min_range - 1}, 'topic':topic}))
    #     print(topic,str(min_range),str(max_range))
    #     body = {
    #         "current": topic + "-" + str(min_range) + "-" + str(max_range),
    #         "next": "r1234-20-30",
    #         "comments": comments,
    #     }
    # ballot = collection.find_one({"_id": ballotspec_id})

    # create a response


    # return response
    
