# import pymongo

# client = pymongo.MongoClient("mongodb://localhost:27017/") 

# db = client['vegetable_db']  

# categories_collection = db['categories']
# vegetables_collection = db['vegetables']


import pymongo 

def get_db():
    client = pymongo.MongoClient("mongodb://localhost:27017/") 
    db = client['vegetable_db']  
    return db


def get_collections():
    db = get_db()
    categories_collection = db['categories']
    vegetables_collection = db['vegetables']
    return categories_collection, vegetables_collection


categories_collection, vegetables_collection = get_collections()
for category in categories_collection.find():
    print(category)
