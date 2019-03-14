import json
from pymongo import MongoClient as my

client = my('localhost', 27017) # Connecting to your local mongo server.
db = client['awake']
collection = db['data']

data = []
with open('file.json') as f:# Give your file's location here.
     for line in f:
         data.append(json.loads(line))


collection.insert(data)
client.close()
