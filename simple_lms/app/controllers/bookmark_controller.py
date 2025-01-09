from flask import request, jsonify
from .. import db
from ..models import Bookmark

def add_bookmark(course_id):
    data = request.get_json()
    new_bookmark = Bookmark(
        user_id=data['user_id'],
        course_id=course_id,
        content_id=data['content_id']
    )
    db.session.add(new_bookmark)
    db.session.commit()
    return jsonify({'message': 'Bookmark added successfully', 'bookmark_id': new_bookmark.id}), 201

def show_bookmarks(user_id):
    bookmarks = Bookmark.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'course_id': bookmark.course_id,
        'content_id': bookmark.content_id
    } for bookmark in bookmarks]), 200

def delete_bookmark(bookmark_id):
    bookmark = Bookmark.query.get(bookmark_id)
    if bookmark is None:
        return jsonify({'message': 'Bookmark not found'}), 404

    db.session.delete(bookmark)
    db.session.commit()
    return jsonify({'message': 'Bookmark deleted successfully'}), 200