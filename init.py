from pymongo import MongoClient
import data

# from urllib.parse import quote_plus
# userame = quote_plus("username")
# password = quote_plus("password")

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
# only display one element with all their keys and values 
print(collection.find_one({ "model": "Trident Z5 RGB"}))
#  {'_id': ObjectId('691a6b4d23007d3767f879e4'), 'manufacturer': 'G.Skill', 'model': 'Trident Z5RGB', 'characteristics': {'capacity': '32GB (2x16GB Kit)', 'generation': 'DDR5', 'speed': '6400 MHz', 'latency': 'CL32', 'form_factor': 'DIMM', 'features': 'RGB lighting, premium design, Intel XMP 3.0 support'}, 'presentation_date': datetime.datetime(2021, 9, 2, 0, 0), 'initial_price_usd': 400, 'updatedAt': datetime.datetime(2025, 12, 9, 3, 22, 48, 42000)}

# To each document in the collection display only two keys (model and initial_price_usd)
for mem in memories:
    print(f"{mem['model']:<20}  U${mem['initial_price_usd']:>7,.2f}")

single = collection.findOne({ 'model': "Trident Z5 RGB"})



client.close()
