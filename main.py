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


def showOne(collection):
    print("\n--- FIND ONE MEMORY MODULE ---")
    model_name = input("Enter the model name to search: ")

    mem = collection.find_one({"model": model_name})
    # print(mem)
        # for mem in memories:
    print(f"{mem['model']:<20}  U${mem['initial_price_usd']:>7,.2f}")
    # Using a case-insensitive regex search
    # mem = collection.find_one({"model": {"$regex": model_name, "$options": "i"}})

    # if mem:
    #     print("\nFound Document:")
    #     print(f"ID: {mem.get('_id')}")
    #     print(f"Manufacturer: {mem.get('manufacturer')}")
    #     print(f"Model: {mem.get('model')}")
    #     print(f"Initial Price: U${mem.get('initial_price_usd'):,.2f}")
    #     print("Characteristics:")
    #     for k, v in mem.get("characteristics", {}).items():
    #         print(f"  - {k}: {v}")
    # else:
    #     print("No memory module found matching that model name.")
    print()
    
def main():
    
    clt = connDB()

    db = clt["hardware"]
    collection = db["memory"]

    while True:
        print("==================================")
        print("      MONGODB HARDWARE MENU       ")
        print("==================================")
        print("1. Show All Memories (Read All)")
        print("2. Find One Memory by Model (Read One)")
        print("3. Add New Memory (Create)")
        print("4. Update Memory Price (Update)")
        print("5. Delete Memory (Delete)")
        print("6. Exit")

        choice = input("\nSelect an option (1-6): ").strip()

        if choice == "1":
            print("Working on it")
            # showAll(collection)
        elif choice == "2":
            showOne(collection)
        elif choice == "6":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 6.\n")

    clt.close()

if __name__ == "__main__":
    main()

'''
{'_id': ObjectId('691a6b4d23007d3767f879e4'), 
'manufacturer': 'G.Skill', 
'model': 'Trident Z5RGB', 
'characteristics': {
    'capacity': '32GB (2x16GB Kit)', 
    'generation': 'DDR5', 'speed': '6400 MHz', 
    'latency': 'CL32', 
    'form_factor': 'DIMM', 
    'features': 'RGB lighting, premium design, Intel XMP 3.0 support'
}, 
'presentation_date': datetime.datetime(2021, 9, 2, 0, 0), 
'initial_price_usd': 400, 
'updatedAt': datetime.datetime(2025, 12, 9, 3, 22, 48, 42000)}
'''