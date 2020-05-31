import json
import os
import uuid
import pymongo
from mode import *
import hashlib
import datetime


# Connection String
client = pymongo.MongoClient(mongosettings[URL])
db = client[mongosettings[MONGODB]]
collection = db[mongosettings[COMMENTSCOLLECTION]]


def create(event, context):
    # get request body
    data = json.loads(event['body'])

    try:
        # create vote to insert
        topic = data["topic"]
        user = data["user"]
        comment = data["comment"]
        now = str(datetime.datetime.now())
        comment_id = collection.find({'topic':topic}).count() +  1
        comment_info = {
                "user": user,
                "comment": comment,
                "time": now
            }
        # write bill to database
        id = topic + "_" + str(comment_id)
        collection.insert_one({"_id":id,'topic':topic, 'number': comment_id, 'comment_info': comment_info})

        # create response
        response = {
            "statusCode": 200,
            "body": json.dumps(comment_info)
        }
    except Exception as e:
        response = {
            "statusCode": 400,
            "body": str(e),
        }

    # return response
    return response


def make_vote_id(pub_key, id, ballotspec_hash, constituency):
    h = hashlib.sha256()
    h.update(str(pub_key).encode('utf-8') +
             str(id).encode('utf-8') +
             str(ballotspec_hash).encode('utf-8') +
             str(constituency).encode('utf-8'))
    return(h.hexdigest())
