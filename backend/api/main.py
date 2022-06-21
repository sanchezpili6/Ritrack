from flask import Blueprint
from flask import request
from bson import json_util, ObjectId
import json

import pymongo

uri = 'mongodb+srv://pili:W5jk9cHJ!@ritrack.kesgjqz.mongodb.net/test'
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
    user = db.Users.find_one({"email": email})
    return parse_json(user)


@main_blueprint.route('/add_user', methods=['POST'])
def add_user():
    content = request.get_json()
    name = content.get('name')
    email = content.get('email')
    password = content.get('password')
    pets = []
    location = ''
    db.Users.insert_one({
        "name": name,
        "email": email,
        "password": password,
        "pets": pets,
        "location": location,
        "is_logged_in": True
    })
    return {"success": True}


@main_blueprint.route('/login', methods=['POST'])
def login():
    content = request.get_json()
    email = content.get('email')
    password = content.get('password')
    user = get_user(email)
    if user['password'] == password:
        try:
            db.Users.update_one(
                {"email": email},
                {"$set": {"is_logged_in": True}}
            )
            return 'success'
        except Exception as e:
            print(e)
            return {'error': 'error logging in'}
    return {'error': 'wrong password'}


@main_blueprint.route('/logout', methods=['POST'])
def logout():
    content = request.get_json()
    email = content.get('email')
    try:
        db.Users.update_one(
            {"email": email},
            {"$set": {"is_logged_in": False}}
        )
        return {'success': True}
    except:
        return {'error': 'error logging out'}


@main_blueprint.route('/get_pet/<id>', methods=['GET'])
def get_pet(id):
    pet = db.Pets.find_one({}, {"_id": id, "name":True})
    print('pet:')
    print(pet)
    return parse_json(pet)


@main_blueprint.route('/add_pet', methods=['POST'])
def add_pet():
    content = request.get_json()
    name = content.get('name')
    characteristics = content.get('characteristics')
    status = content.get('status')
    human = content.get('human')
    location = content.get('location')
    _id = db.Pets.insert_one({
        "name": name,
        "characteristics": characteristics,
        "status": status,
        "human": human,
        "location": location
    })
    db.Users.update_one(
        {"_id": ObjectId(human)},
        {"$push": {"pets": _id.inserted_id}}
    )
    print('just id')
    print(_id)
    print('_id.inserted_id')
    print(_id.inserted_id)
    return {"success": True}


@main_blueprint.route('/edit_pet', methods=['POST'])
def edit_pet():
    content = request.get_json()
    id = content['id']
    data = dict(content)
    if 'characteristics' in data:
        data['characteristics'] = [char.strip() for char in data['characteristics'].strip('[]').split(',')]
    try:
        data.pop('id')
        db.Pets.update_one(
            {"_id": ObjectId(id)},
            {"$set": data}
        )
        return {'success': True}
    except:
        return {'error': 'error editing pet'}


@main_blueprint.route('/get_lost_pets', methods=['GET'])
def get_lost_pets():
    pets = db.get_collection('Pets').find({"status": "Lost"})
    return pets.count()


@main_blueprint.route('/get_found_pets', methods=['GET'])
def get_found_pets():
    pets = db.Pets.find(
        filter = {
            "status": "Found"
        },
        allow_partial_results = False
    )
    return parse_json(pets)

@main_blueprint.route('/add_found_pet', methods=['POST'])
def add_found_pet():
    content = request.get_json()
    name = content.get('name')
    email = content.get('email')
    characteristics = content.get('characteristics')
    status = 'Found'
    human = 'unknown'
    location = content.get('location')
    db.Pets.insert_one({
        "name": name,
        "characteristics": characteristics,
        "status": status,
        "human": human,
        "email": email,
        "location": location
    })
    return {"success": True}
