import pprint
import json
import pymongo
from pymongo import MongoClient as my

client = my('localhost', 27017)
db = client.experiment1_db #input your own database name.
coll = db.data #input your own collection name.
print coll.count()

for document in coll.find({}):
   print "\n"
   pprint.pprint(document)
