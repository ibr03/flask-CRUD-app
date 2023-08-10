from flask_restful import Resource, reqparse
from app.models.user import User

class UserListResource(Resource):
    def get(self):
        users = User.get_all()
        return users, 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Name field is required')
        parser.add_argument('email', type=str, required=True, help='Email field is required')
        parser.add_argument('password', type=str, required=True, help='Password field is required')
        data = parser.parse_args()

        user = User(data['name'], data['email'], data['password'])
        user.save()
        return {'message': 'User created successfully!'}, 201

class UserResource(Resource):
    def get(self, user_id):
        user = User.get_by_id(user_id)
        if user:
            return user, 200
        else:
            return {'message': 'User not found'}, 404

    def put(self, user_id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True, help='Name field is required')
        parser.add_argument('email', type=str, required=True, help='Email field is required')
        parser.add_argument('password', type=str, required=True, help='Password field is required')
        data = parser.parse_args()

        user = User(data['name'], data['email'], data['password'])
        user.update(user_id)
        return {'message': 'User updated successfully!'}, 200

    def delete(self, user_id):
        User.delete(user_id)
        return {'message': 'User deleted successfully!'}, 200
