from flask import jsonify, request
from . import app
from .models import User

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        users = User.get_all()
        return jsonify(users), 200
    elif request.method == 'POST':
        data = request.get_json()
        user = User(data['name'], data['email'], data['password'])
        user.save()
        return jsonify({'message': 'User created successfully!'}), 201

@app.route('/users/<string:user_id>', methods=['GET', 'PUT', 'DELETE'])
def user_detail(user_id):
    if request.method == 'GET':
        user = User.get_by_id(user_id)
        if user:
            return jsonify(user), 200
        else:
            return jsonify({'message': 'User not found'}), 404
    elif request.method == 'PUT':
        data = request.get_json()
        user = User(data['name'], data['email'], data['password'])
        user.update(user_id)
        return jsonify({'message': 'User updated successfully!'}), 200
    elif request.method == 'DELETE':
        User.delete(user_id)
        return jsonify({'message': 'User deleted successfully!'}), 200
