from . import db

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)  # Store hashed passwords
    phone = db.Column(db.String(15), nullable=True)
    description = db.Column(db.Text, nullable=True)
    profile_picture = db.Column(db.String(200), nullable=True)

    # Relationships
    courses = db.relationship('Enrollment', backref='user', lazy=True)

# Course Model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    max_students = db.Column(db.Integer, default=10)  # Default maximum students

    # Relationships
    students = db.relationship('Enrollment', backref='course', lazy=True)
    comments = db.relationship('Comment', backref='course', lazy=True)

# Enrollment Model (Many-to-Many relationship between User and Course)
class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

# Comment Model
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    moderated = db.Column(db.Boolean, default=False)

# Activity Dashboard Model
class ActivityDashboard(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    courses_joined = db.Column(db.Integer, default=0)
    courses_created = db.Column(db.Integer, default=0)
    comments_written = db.Column(db.Integer, default=0)
    content_completed = db.Column(db.Integer, default=0)

# Announcement Model
class Announcement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

# Completion Tracking Model
class CompletionTracking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    content_id = db.Column(db.Integer, nullable=False)  # Assuming content_id refers to some content

# Feedback Model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)

# Bookmark Model
class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    content_id = db.Column(db.Integer, nullable=False)  # Assuming content_id refers to some content

# Category Model
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Content Model (for content approval workflow)
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    published = db.Column(db.Boolean, default=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)

# Rate Limiting Model (optional, if you want to track limits)
class RateLimit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    ip_address = db.Column(db.String(45), nullable=False)  # For IPv6 support
    register_attempts = db.Column(db.Integer, default=0)
    comment_attempts = db.Column(db.Integer, default=0)
    course_creation_attempts = db.Column(db.Integer, default=0)
    content_creation_attempts = db.Column(db.Integer, default=0)
