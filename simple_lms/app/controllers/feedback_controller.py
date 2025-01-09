from flask import request, jsonify
from .. import db
from ..models import Feedback

def add_feedback(course_id):
    data = request.get_json()
    new_feedback = Feedback(
        course_id=course_id,
        user_id=data['user_id'],
        content=data['content']
    )
    db.session.add(new_feedback)
    db.session.commit()
    return jsonify({'message': 'Feedback added successfully', 'feedback_id': new_feedback.id}), 201

def show_feedback(course_id):
    feedbacks = Feedback.query.filter_by(course_id=course_id).all()
    return jsonify([{
        'user_id': feedback.user_id,
        'content': feedback.content
    } for feedback in feedbacks]), 200

def edit_feedback(feedback_id):
    feedback = Feedback.query.get(feedback_id)
    if feedback is None:
        return jsonify({'message': 'Feedback not found'}), 404

    data = request.get_json()
    feedback.content = data.get('content', feedback.content)

    db.session.commit()
    return jsonify({'message': 'Feedback updated successfully'}), 200

def delete_feedback(feedback_id):
    feedback = Feedback.query.get(feedback_id)
    if feedback is None:
        return jsonify({'message': 'Feedback not found'}), 404

    db.session.delete(feedback)
    db.session.commit()
    return jsonify({'message': 'Feedback deleted successfully'}), 200