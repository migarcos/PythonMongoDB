from pymongo import MongoClient
import data

from urllib.parse import quote_plus
userame = quote_plus("username")
password = quote_plus("password")

# uri = MongoClient("mongodb+srv://<username>:<password>@cluster.mongodb.net/")

client = MongoClient(data.uri)

try:
    client.admin.command("ping")
    print("Connected successfully")
except Exception as e:
    raise Exception(
        "The following error occurred: ", e)

db = client["hardware"]
collection = db["memory"]

memories = collection.find()

for mem in memories:
    print(f"{mem['model']:<20}  U${mem['initial_price_usd']:>7,.2f}")


client.close()
