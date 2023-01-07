import pymongo

client = pymongo.MongoClient("mongodb+srv://Dimo23:Dimo10796@dimo23.hy1mjfh.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"vaibhav",
    "email":"vaibhavdimri10796@gmail.com",
    "surname":"dimri"
}

db1 = client['m1']
coll = db1['test']
coll.insert_one(d)

