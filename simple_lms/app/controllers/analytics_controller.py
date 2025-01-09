from flask import jsonify
from ..models import Course, Enrollment, Comment, Feedback, Content

def course_analytics(course_id):
    # Fetch the course to ensure it exists
    course = Course.query.get(course_id)
    if course is None:
        return jsonify({'message': 'Course not found'}), 404

    # Calculate the number of enrolled students
    member_count = Enrollment.query.filter_by(course_id=course_id).count()

    # Calculate the number of comments for the course
    comment_count = Comment.query.filter_by(course_id=course_id).count()

    # Calculate the number of feedback entries for the course
    feedback_count = Feedback.query.filter_by(course_id=course_id).count()

    # Count the number of content items associated with the course
    content_count = Content.query.filter_by(course_id=course_id).count()  # Use query to count directly

    return jsonify({
        'member_count': member_count,
        'content_count': content_count,
        'comment_count': comment_count,
        'feedback_count': feedback_count
    }), 200