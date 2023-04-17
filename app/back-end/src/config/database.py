from pymongo.mongo_client import MongoClient
from dotenv import dotenv_values

config = dotenv_values()

client = MongoClient(config["MONGO_URL"])

try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
