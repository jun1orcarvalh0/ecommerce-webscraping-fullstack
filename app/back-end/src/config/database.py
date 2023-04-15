from pymongo.mongo_client import MongoClient

URL = "mongodb+srv://root:uCxXEfFCz8qpBrzm@cluster0.p9uyrnv.mongodb.net/ecommerce_webscraping_db?retryWrites=true&w=majority"

client = MongoClient(URL)
db = client.get_database('ecommerce_webscraping_db')
buscape_colletion = db.buscape

try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


def find_news():
    return buscape_colletion.find_one({})


news = find_news()
print(news)
