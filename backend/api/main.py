from flask import Blueprint
from flask import request
from bson import json_util, ObjectId
import json

import pymongo
uri = ''
client = pymongo.MongoClient(uri)
db = client.Ritrack

main_blueprint = Blueprint('main', __name__)


def parse_json(data):
    return json.loads(json_util.dumps(data))


@main_blueprint.route('/test', methods=['GET'])
def test():
    return 'Hola'


@main_blueprint.route('/get_user/<email>', methods=['GET'])
def get_user(email):
    user = db.Users.find_one({ "email": email })
    return parse_json(user)


@main_blueprint.route('/add_user', methods=['POST'])
def add_user():
    email = request.form['email']
    password = request.form['password']
    name = request.form['name']
    pets = request.form['pets'].strip('[]').split(',')
    location = request.form['location']
    try:
        db.Users.insert_one({
            "name": name,
            "email": email,
            "password": password,
            "pets": pets,
            "location": location,
            "is_logged_in": True
        })
        return { "success": True }
    except DuplicateKeyError:
        return {"error": "A user with the given email already exists."}


@main_blueprint.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user = get_user(email)
    if user['password'] == password:
        try:
            db.Users.update_one(
                { "email": email },
                { "$set": {"is_logged_in": True} }
            )
            return { 'success': user['password'] == password }
        except Exception as e:
            print(e)
            return { 'error': 'error logging in' }
    return { 'error': 'wrong password' }


@main_blueprint.route('/logout', methods=['POST'])
def logout():
    email = request.form['email']
    try:
        db.Users.update_one(
            { "email": email },
            { "$set": {"is_logged_in": False} }
        )
        return { 'success': True }
    except:
        return { 'error': 'error logging out' }
