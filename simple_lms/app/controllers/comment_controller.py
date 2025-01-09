from flask import request, jsonify
from .. import db
from ..models import Comment

def add_comment(course_id):
    data = request.get_json()
    new_comment = Comment(content=data['content'],user_id=data['user_id'] , course_id=course_id)
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({'message': 'Comment added successfully', 'comment_id': new_comment.id}), 201

def moderate_comment(comment_id):
    comment = Comment.query.get(comment_id)
    if comment:
        comment.moderated = True
        db.session.commit()
        return jsonify({'message': 'Comment moderated successfully'}), 200
    return jsonify({'message': 'Comment not found'}), 404