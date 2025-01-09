from flask import Blueprint
from .controllers.user_controller import register_user
from .controllers.course_controller import batch_enroll, create_course
from .controllers.comment_controller import add_comment, moderate_comment
from .controllers.analytics_controller import course_analytics
from .controllers.profile_controller import show_profile, edit_profile
from .controllers.announcement_controller import create_announcement, show_announcements, edit_announcement, delete_announcement
from .controllers.completion_controller import add_completion_tracking, show_completion, delete_completion
from .controllers.feedback_controller import add_feedback, show_feedback, edit_feedback, delete_feedback
from .controllers.bookmark_controller import add_bookmark, show_bookmarks, delete_bookmark
from .controllers.category_controller import add_category, show_categories, delete_category
from .controllers.approval_controller import update_content, publish_content, unpublish_content
from .controllers.rate_limiting_controller import limit_register, limit_comment, limit_course_creation, limit_content_creation
from .controllers.user_activity_controller import user_activity_dashboard

app = Blueprint('app', __name__)

# User routes
@app.route('/register', methods=['POST'])
def register():
    # return jsonify({'message': 'User registered successfully'}), 201
    return register_user()

# Course routes
@app.route('/courses/<int:course_id>/enroll', methods=['POST'])
def enroll_students(course_id):
    return batch_enroll(course_id)

@app.route('/courses', methods=['POST'])
def create_new_course():
    return create_course()

# Comment routes
@app.route('/courses/<int:course_id>/comments', methods=['POST'])
def post_comment(course_id):
    return add_comment(course_id)

@app.route('/comments/<int:comment_id>/moderate', methods=['PATCH'])
def moderate_comment_route(comment_id):
    return moderate_comment(comment_id)

# Analytics route
@app.route('/courses/<int:course_id>/analytics', methods=['GET'])
def get_course_analytics(course_id):
    return course_analytics(course_id)

# User Activity Dashboard route
@app.route('/users/<int:user_id>/activity', methods=['GET'])
def get_user_activity(user_id):
    return user_activity_dashboard(user_id)

# User Profile routes
@app.route('/users/<int:user_id>/profile', methods=['GET'])
def get_user_profile(user_id):
    return show_profile(user_id)

@app.route('/users/<int:user_id>/profile', methods=['PUT'])
def update_user_profile(user_id):
    return edit_profile(user_id)

# Announcement routes
@app.route('/courses/<int:course_id>/announcements', methods=['POST'])
def create_course_announcement(course_id):
    return create_announcement(course_id)

@app.route('/courses/<int:course_id>/announcements', methods=['GET'])
def get_course_announcements(course_id):
    return show_announcements(course_id)

@app.route('/announcements/<int:announcement_id>', methods=['PUT'])
def update_announcement(announcement_id):
    return edit_announcement(announcement_id)

@app.route('/announcements/<int:announcement_id>', methods=['DELETE'])
def remove_announcement(announcement_id):
    return delete_announcement(announcement_id)

# Completion Tracking routes
@app.route('/courses/<int:course_id>/completion', methods=['POST'])
def track_completion(course_id):
    return add_completion_tracking(course_id)

@app.route('/courses/<int:course_id>/completion', methods=['GET'])
def get_completion(course_id):
    return show_completion(course_id)

@app.route('/completion/<int:completion_id>', methods=['DELETE'])
def remove_completion(completion_id):
    return delete_completion(completion_id)

# Feedback routes
@app.route('/courses/<int:course_id>/feedback', methods=['POST'])
def submit_feedback(course_id):
    return add_feedback(course_id)

@app.route('/courses/<int:course_id>/feedback', methods=['GET'])
def get_feedback(course_id):
    return show_feedback(course_id)

@app.route('/feedback/<int:feedback_id>', methods=['PUT'])
def update_feedback(feedback_id):
    return edit_feedback(feedback_id)

@app.route('/feedback/<int:feedback_id>', methods=['DELETE'])
def remove_feedback(feedback_id):
    return delete_feedback(feedback_id)

# Bookmark routes
@app.route('/courses/<int:course_id>/bookmarks', methods=['POST'])
def create_bookmark(course_id):
    return add_bookmark(course_id)

@app.route('/users/<int:user_id>/bookmarks', methods=['GET'])
def get_user_bookmarks(user_id):
    return show_bookmarks(user_id)

@app.route('/bookmarks/<int:bookmark_id>', methods=['DELETE'])
def delete_user_bookmark(bookmark_id):
    return delete_bookmark(bookmark_id)

# Category routes
@app.route('/categories', methods=['POST'])
def create_category():
    return add_category()

@app.route('/categories', methods=['GET'])
def list_categories():
    return show_categories()

@app.route('/categories/<int:category_id>', methods=['DELETE'])
def remove_category(category_id):
    return delete_category(category_id)

# Content Approval Workflow routes
@app.route('/content/<int:content_id>', methods=['PUT'])
def update_content_route(content_id):
    return update_content(content_id)

@app.route('/content/<int:content_id>/publish', methods=['POST'])
def publish_content_route(content_id):
    return publish_content(content_id)

@app.route('/content/<int:content_id>/unpublish', methods=['POST'])
def unpublish_content_route(content_id):
    return unpublish_content(content_id)