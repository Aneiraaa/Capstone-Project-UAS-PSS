from flask import request, jsonify
from .. import db
from ..models import Category

def add_category():
    data = request.get_json()
    new_category = Category(name=data['name'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify({'message': 'Category added successfully', 'category_id': new_category.id}), 201

def show_categories():
    categories = Category.query.all()
    return jsonify([{
        'id': category.id,
        'name': category.name
    } for category in categories]), 200

def delete_category(category_id):
    category = Category.query.get(category_id)
    if category is None:
        return jsonify({'message': 'Category not found'}), 404

    db.session.delete(category)
    db.session.commit()
    return jsonify({'message': 'Category deleted successfully'}), 200