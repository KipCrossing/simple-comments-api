# simple-comments-api
A simple serverless api (python) for reading and making comments on a topic


## Public Contracts

```
endpoints:
  GET - https://nakkqadvg1.execute-api.ap-southeast-2.amazonaws.com/dev/comment/{command}
  POST - https://nakkqadvg1.execute-api.ap-southeast-2.amazonaws.com/dev/comment
```

### Post a Comment

**POST**

```
https://nakkqadvg1.execute-api.ap-southeast-2.amazonaws.com/dev/comment
```

Example body:

```
{
"topic": "r1234",
"user": "David",
"comment": "This is great!"
}
```

### Get Comments of Topic

**GET**

```
https://nakkqadvg1.execute-api.ap-southeast-2.amazonaws.com/dev/comment/r1234
```

Example response:


```
[
    {
        "_id": "r1234_2",
        "topic": "r1234",
        "number": 2,
        "comment_info": {
            "user": "Jess",
            "comment": "It so is!",
            "time": "2020-05-31 10:27:50.171938"
        }
    },
    {
        "_id": "r1234_1",
        "topic": "r1234",
        "number": 1,
        "comment_info": {
            "user": "david",
            "comment": "This is great!",
            "time": "2020-05-31 10:27:04.222391"
        }
    }
]
```

## Getting started

### On first time

```
sudo apt-get install nodejs

sudo apt-get install curl software-properties-common

curl -sL https://deb.nodesource.com/setup_12.x | sudo bash -

sudo npm install -g serverless
```

[Install MongoDB](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-debian/#install-mongodb-community-edition)

Install requirements

```
pip3 install -r requirements.txt
npm install
```

### On every startup

### Dev (offlline)

Start MongoDB

```
sudo systemctl start mongod
```

'python3 update_bills_db.py' _may be run on loop every few hours to update DB_

we haven't got a good way to update the issues collection yet

Run serverless offline

```
serverless offline
```

Ctrl+C to stop _serverless offline_