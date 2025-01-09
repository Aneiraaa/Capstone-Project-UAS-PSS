from flask import request, jsonify
from .. import db
from ..models import User

def show_profile(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'message': 'User  not found'}), 404
    return jsonify({
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'phone': user.phone,
        'description': user.description,
        'profile_picture': user.profile_picture
    }), 200

def edit_profile(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'message': 'User  not found'}), 404

    data = request.get_json()
    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)
    user.email = data.get('email', user.email)
    user.phone = data.get('phone', user.phone)
    user.description = data.get('description', user.description)
    user.profile_picture = data.get('profile_picture', user.profile_picture)

    db.session.commit()
    return jsonify({'message': 'Profile updated successfully'}), 200