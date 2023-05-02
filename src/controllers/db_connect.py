import pymongo

# establish a connection to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# select the database
db = client["setlist"]
