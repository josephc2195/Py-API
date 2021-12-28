from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

class Users(Resource):
        def get(self):
                data = pd.read_csv('https://raw.githubusercontent.com/josephc2195/Py-API/master/Datasets/users.csv')
                data = data.to_dict()
                return {'data': data}, 200
        
        def post(self):
                parser = reqparse.RequestParser()
                parser.add_argument('userId', required=True, type=int)
                parser.add_argument('name', required=True)
                parser.add_argument('city', required=True)
                args = parser.parse_args()
                
                data = pd.read_csv('https://raw.githubusercontent.com/josephc2195/Py-API/master/Datasets/users.csv')
                if args['userId'] in data['userId']:
                        return {
                                'message': f"{args['userId']} is already taken."
                        }, 409
                else:
                        data=data.append({
                                'userId':args['userId'],
                                'name':args['name'],
                                'city':args['city'],
                                'locations':[]
                        }, ignore_index=True)
                        return {'data':data.to_dict()}, 200

                
                
class Locations(Resource):
        pass

api.add_resource(Users, '/users')
api.add_resource(Locations, '/locations')

if __name__ == '__main__':
        app.run(debug=True)
