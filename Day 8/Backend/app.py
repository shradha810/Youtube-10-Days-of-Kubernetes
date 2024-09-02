from flask import Flask, request, jsonify
import pymongo
import os

Mongo = os.environ.get('MONGO')
client = pymongo.MongoClient(Mongo)
### cluster: Cluster0 database:test collection:flask-signup ###
db = client.test
collection = db['flask-signup']

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Backend is running'})

@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.json) 
    collection.insert_one(form_data)
    return 'Data Added to mongoDB'

@app.route('/data')
def data():
    content = list(collection.find())
    print(content)
    for elm in content:
        del(elm['_id'])
    return jsonify({'Content': content})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8500,debug=True)