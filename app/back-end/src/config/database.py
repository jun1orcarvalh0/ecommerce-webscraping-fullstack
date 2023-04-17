from pymongo.mongo_client import MongoClient
from decouple import config

MONGO_DB_URL = config("MONGO_URL")

client = MongoClient(MONGO_DB_URL)

try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
