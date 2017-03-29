# m.py

# Manuel Moya Ferrer
# Example of managing mongoDB from python driver.

def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.usersDB
    return db

def add_user(db):
    db.user.insert({"name" : "Manuel"})
    
def get_user(db):
    return db.user.find_one()

if __name__ == "__main__":

    db = get_db() 
    add_user(db)
    print get_user(db)