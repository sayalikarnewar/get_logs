import pymongo

async def setupDB():
    client = pymongo.MongoClient('mongodb://localhost:27017')
    db = client.folloDB
    return db