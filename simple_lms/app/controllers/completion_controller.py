from flask import request, jsonify
from .. import db
from ..models import CompletionTracking

def add_completion_tracking(course_id):
    data = request.get_json()
    new_completion = CompletionTracking(
        course_id=course_id,
        user_id=data['user_id'],
        content_id=data['content_id']
    )
    db.session.add(new_completion)
    db.session.commit()
    return jsonify({'message': 'Completion tracking added successfully', 'completion_id': new_completion.id}), 201

def show_completion(course_id):
    completions = CompletionTracking.query.filter_by(course_id=course_id).all()
    return jsonify([{
        'user_id': completion.user_id,
        'content_id': completion.content_id
    } for completion in completions]), 200

def delete_completion(completion_id):
    completion = CompletionTracking.query.get(completion_id)
    if completion is None:
        return jsonify({'message': 'Completion not found'}), 404

    db.session.delete(completion)
    db.session.commit()
    return jsonify({'message': 'Completion deleted successfully'}), 200