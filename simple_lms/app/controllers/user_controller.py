from flask import request, jsonify
from werkzeug.security import generate_password_hash
from .. import db
from ..models import User

def register_user():
    data = request.get_json()

    # Hash the password before storing it
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256', salt_length=16)

    new_user = User(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        password=hashed_password,  # Store the hashed password
        phone=data.get('phone'),
        description=data.get('description'),
        profile_picture=data.get('profile_picture')
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User  registered successfully', 'user_id': new_user.id}), 201