from flask import Flask, request, jsonify
import pprint
import json
import pymongo
from bson.json_util import dumps
from pymongo import MongoClient as my
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)



app = Flask(__name__)

@app.route('/get_data', methods = ['GET'])
def get_data():
           client = my('localhost', 27017) 
           flask = client['experiment1_db'] # select your database.
           scan = flask.data.find({}) # "data" represents the specific collection we are intrested in.
           my_list = [] 
           for x in scan: 
             my_list.append([x])
           return JSONEncoder().encode(my_list)


if __name__ == '__main__':
    app.run(debug=True)



