from flask import jsonify
from ..models import User, Course, Enrollment, Comment, CompletionTracking

def user_activity_dashboard(user_id):
    # Fetch the user to ensure they exist
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'message': 'User  not found'}), 404

    # Calculate the number of courses the user is enrolled in
    enrolled_courses_count = Enrollment.query.filter_by(user_id=user_id).count()

    # Calculate the number of comments written by the user
    comments_count = Comment.query.filter_by(user_id=user_id).count()

    # Calculate the number of content items completed by the user
    completed_content_count = CompletionTracking.query.filter_by(user_id=user_id).count()  # Assuming user_id is the field in CompletionTracking model

    return jsonify({
        'enrolled_courses_count': enrolled_courses_count,
        'comments_count': comments_count,
        'completed_content_count': completed_content_count
    }), 200