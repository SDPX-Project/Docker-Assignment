from flask import Flask, request, jsonify,make_response
import database

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return "SPDX Backend"

@app.route('/user', methods=['GET'])
def getAllUser():
    user = database.get_all_data()
    return jsonify(user)

@app.route('/user/<id>', methods=['GET'])
def getUserById(id):
    user = database.get_data_byid(id)
    return make_response(jsonify(user), 200)

@app.route('/user/add', methods=['POST'])
def createUser():
    data = request.get_json()
    if not(data['name'] and data['age']):
        return "data require"
    database.inser_data(data['name'], data['age'])
    return make_response(jsonify({'message': "create user success"}),200)


@app.route('/user/update', methods=['PUT'])
def updateUser():
    _id = request.json['id']
    name = request.json['name']
    age = request.json['age']
    if not (_id and name and age and request.method == 'PUT'):
        return "data require"

    database.update_data(_id, name, age)
    return make_response(jsonify({'message' : 'success'}),200)


@app.route('/user/delete/<id>', methods=['DELETE'])
def deleteUser(id):
    database.delete_data(id)
    return make_response(jsonify({'message': "success"}),200)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)