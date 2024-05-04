import json
import re
from flask import Flask, request, jsonify

app = Flask(__name__)
DATA_FILE = 'users.json'

def read_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except (IOError, json.JSONDecodeError):
        return []  

def write_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def is_valid_phone(phone):
    return re.fullmatch(r'\d{10}', phone) is not None

def is_valid_name(name):
    return re.fullmatch(r'[A-Za-z ]+', name) is not None

def is_valid_email(email):
    return re.fullmatch(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', email) is not None

@app.route('/users', methods=['GET', 'POST'])
def manage_users():
    users = read_data()
    if request.method == 'POST':
        user_data = request.get_json()
        if not all([user_data.get('name'), user_data.get('phone'), user_data.get('email')]):
            return jsonify({'error': 'Missing name, phone or email'}), 400
        
        if not is_valid_name(user_data['name']):
            return jsonify({'error': 'Invalid name. Name should only contain letters.'}), 400
        
        if not is_valid_phone(user_data['phone']):
            return jsonify({'error': 'Invalid phone number. Phone number should be 10 digits long.'}), 400
        
        if not is_valid_email(user_data['email']):
            return jsonify({'error': 'Invalid email format.'}), 400

        users.append(user_data)
        write_data(users)
        return jsonify(user_data), 201

    elif request.method == 'GET':
        return jsonify(users), 200

@app.route('/users/<int:user_index>', methods=['GET', 'PUT', 'DELETE'])
def user(user_index):
    users = read_data()
    if user_index < 0 or user_index >= len(users):
        return jsonify({'error': 'User not found'}), 404

    if request.method == 'GET':
        return jsonify(users[user_index]), 200

    elif request.method == 'PUT':
        user_data = request.get_json()
        if not all([user_data.get('name'), user_data.get('phone'), user_data.get('email')]):
            return jsonify({'error': 'Missing name, phone or email'}), 400
        
        if not is_valid_name(user_data['name']):
            return jsonify({'error': 'Invalid name. Name should only contain letters.'}), 400
        
        if not is_valid_phone(user_data['phone']):
            return jsonify({'error': 'Invalid phone number. Phone number should be 10 digits long.'}), 400
        
        if not is_valid_email(user_data['email']):
            return jsonify({'error': 'Invalid email format.'}), 400

        users[user_index] = user_data
        write_data(users)
        return jsonify(user_data), 200

    elif request.method == 'DELETE':
        users.pop(user_index)
        write_data(users)
        return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
