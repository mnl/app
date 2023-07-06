#!/usr/bin/python3
from flask import Flask
from flask_restful import Resource, Api, reqparse
import sys

def hello():
    name = sys.argv[1] if len(sys.argv) >= 2 else "Default"
    print(f"Hello, {name}!")

app = Flask(__name__)
api = Api(app)

PEOPLE = {
  '1': {'name': 'Alice', 'age': 23, 'spec': 'dev'},
  '2': {'name': 'Bob', 'age': 20, 'spec': 'dev'},
  '3': {'name': 'Cindy', 'age': 21, 'spec': 'ops'},
  '4': {'name': 'Dave', 'age': 22, 'spec': 'hr'},
}

class apiroot(Resource):
    def get(self):
        return {'status': 'ok'}

class PeopleList(Resource):
    def get(self):
        return PEOPLE
    def post(self): pass

class Person(Resource):
  def get(self, person_id):
      return PEOPLE.get(person_id, ("Not found", 404))

  def put(self, person_id): pass

  def delete(self, person_id):
      if person_id not in PEOPLE:
          return "Not found", 404
      del PEOPLE[person_id]
      return '', 204

api.add_resource(Person, '/api/people/<person_id>')

api.add_resource(PeopleList, '/api/people/')

api.add_resource(apiroot, '/api')

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)
