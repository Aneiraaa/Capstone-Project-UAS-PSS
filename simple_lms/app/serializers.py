from .models import User, Course, Comment, Enrollment, Announcement, CompletionTracking, Feedback, Bookmark, Category, CourseAnalytics

# User Serializer
def user_to_dict(user):
    return {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'phone': user.phone,
        'description': user.description,
        'profile_picture': user.profile_picture
    }

# Course Serializer
def course_to_dict(course):
    return {
        'id': course.id,
        'title': course.title,
        'description': course.description,
        'students': [enrollment.user_id for enrollment in course.students],
        'comments': [comment_to_dict(comment) for comment in course.comments]
    }

# Comment Serializer
def comment_to_dict(comment):
    return {
        'id': comment.id,
        'content': comment.content,
        'moderated': comment.moderated,
        'course_id': comment.course_id
    }

# Enrollment Serializer
def enrollment_to_dict(enrollment):
    return {
        'id': enrollment.id,
        'user_id': enrollment.user_id,
        'course_id': enrollment.course_id
    }

# Announcement Serializer
def announcement_to_dict(announcement):
    return {
        'id': announcement.id,
        'course_id': announcement.course_id,
        'content': announcement.content,
        'date': announcement.date.isoformat()  # Convert datetime to ISO format
    }

# Completion Tracking Serializer
def completion_to_dict(completion):
    return {
        'id': completion.id,
        'user_id': completion.user_id,
        'course_id': completion.course_id,
        'content_id': completion.content_id
    }

# Feedback Serializer
def feedback_to_dict(feedback):
    return {
        'id': feedback.id,
        'course_id': feedback.course_id,
        'user_id': feedback.user_id,
        'content': feedback.content
    }

# Bookmark Serializer
def bookmark_to_dict(bookmark):
    return {
        'id': bookmark.id,
        'user_id': bookmark.user_id,
        'course_id': bookmark.course_id,
        'content_id': bookmark.content_id
    }

# Category Serializer
def category_to_dict(category):
    return {
        'id': category.id,
        'name': category.name
    }

# Course Content Serializer
def content_to_dict(content):
    return {
        'id': content.id,
        'title': content.title
    }