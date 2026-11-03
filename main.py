from pymongo import MongoClient
import data

def connDB():

    client = MongoClient(data.uri)
    
    try:
        client.admin.command("ping")
        print("Connected successfully")
    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)

    return(client)


def showOne():
    print()
    
def main():
    
    clt = connDB()

    db = clt["hardware"]
    collection = db["memory"]

    memories = collection.find()

    for mem in memories:
        print(f"{mem['model']:<20}  U${mem['initial_price_usd']:>7,.2f}")

    clt.close()

if __name__ == "__main__":
    main()