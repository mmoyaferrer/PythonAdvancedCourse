# m.py

# Manuel Moya Ferrer
# Example of managing mongoDB from python driver.

def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.userDataBase
    return db

def add_user(db,name,surname,occupation):
    db.userDataBase.insert({"name" : name, "skill" : surname, "occupation" : occupation})
    
def get_user(db,occupation):
    return db.userDataBase.find_one({"occupation" : occupation})

if __name__ == "__main__":

	# Obtaining database from get_db method
    db = get_db() 

    # Adding five users to database
    add_user(db,"Manuel","Ferrer","Telecom. Engineer")
    add_user(db,"Marc","Branson","Medician")
    add_user(db,"Adam","Branson","English Teacher")
    add_user(db,"Daniel","Bell","RF Engineer")
    add_user(db,"Tom","Hanks","Actor")

    # Get a Telecom. engineer of database and show
    print get_user(db,"Telecom. Engineer")