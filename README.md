# simple-comments-api
A simple serverless api (python) for reading and making comments on a topic


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

Populate/update the DB

```
python3 update_bills_db.py
python3 update_issues_db.py
python3 update_ballotspecs_db.py
python3 update_results_db.py
```

'python3 update_bills_db.py' _may be run on loop every few hours to update DB_

we haven't got a good way to update the issues collection yet

Run serverless offline

```
serverless offline
```

Ctrl+C to stop _serverless offline_