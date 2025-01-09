from flask import request, jsonify
from .. import db
from ..models import RateLimit
from datetime import datetime, timedelta

# Constants for rate limiting
REGISTER_LIMIT = 5  # Max 5 registrations per day
COMMENT_LIMIT = 10   # Max 10 comments per hour
COURSE_CREATION_LIMIT = 1  # Max 1 course creation per day
CONTENT_CREATION_LIMIT = 10  # Max 10 content creations per hour

def limit_register():
    ip_address = request.remote_addr
    rate_limit = RateLimit.query.filter_by(ip_address=ip_address).first()

    if rate_limit is None:
        rate_limit = RateLimit(ip_address=ip_address, register_attempts=1, last_register_attempt=datetime.now())
        db.session.add(rate_limit)
    else:
        # Check if the last attempt was within the last 24 hours
        if datetime.now() - rate_limit.last_register_attempt < timedelta(days=1):
            if rate_limit.register_attempts >= REGISTER_LIMIT:
                return jsonify({'message': 'Registration limit reached. Try again later.'}), 429
            else:
                rate_limit.register_attempts += 1
        else:
            rate_limit.register_attempts = 1  # Reset count after 24 hours
            rate_limit.last_register_attempt = datetime.now()

    db.session.commit()
    return jsonify({'message': 'Registration successful.'}), 200

def limit_comment():
    user_id = request.json.get('user_id')
    rate_limit = RateLimit.query.filter_by(user_id=user_id).first()

    if rate_limit is None:
        rate_limit = RateLimit(user_id=user_id, comment_attempts=1, last_comment_attempt=datetime.now())
        db.session.add(rate_limit)
    else:
        # Check if the last attempt was within the last hour
        if datetime.now() - rate_limit.last_comment_attempt < timedelta(hours=1):
            if rate_limit.comment_attempts >= COMMENT_LIMIT:
                return jsonify({'message': 'Comment limit reached. Try again later.'}), 429
            else:
                rate_limit.comment_attempts += 1
        else:
            rate_limit.comment_attempts = 1  # Reset count after 1 hour
            rate_limit.last_comment_attempt = datetime.now()

    db.session.commit()
    return jsonify({'message': 'Comment submitted successfully.'}), 200

def limit_course_creation():
    user_id = request.json.get('user_id')
    rate_limit = RateLimit.query.filter_by(user_id=user_id).first()

    if rate_limit is None:
        rate_limit = RateLimit(user_id=user_id, course_creation_attempts=1, last_course_creation_attempt=datetime.now())
        db.session.add(rate_limit)
    else:
        # Check if the last attempt was within the last 24 hours
        if datetime.now() - rate_limit.last_course_creation_attempt < timedelta(days=1):
            if rate_limit.course_creation_attempts >= COURSE_CREATION_LIMIT:
                return jsonify({'message': 'Course creation limit reached. Try again later.'}), 429
            else:
                rate_limit.course_creation_attempts += 1
        else:
            rate_limit.course_creation_attempts = 1  # Reset count after 24 hours
            rate_limit.last_course_creation_attempt = datetime.now()

    db.session.commit()
    return jsonify({'message': 'Course created successfully.'}), 200

def limit_content_creation():
    user_id = request.json.get('user_id')
    rate_limit = RateLimit.query.filter_by(user_id=user_id).first()

    if rate_limit is None:
        rate_limit = RateLimit(user_id=user_id, content_creation_attempts=1, last_content_creation_attempt=datetime.now())
        db.session.add(rate_limit)
    else:
        # Check if the last attempt was within the last hour
        if datetime.now() - rate_limit.last_content_creation_attempt < timedelta(hours=1):
            if rate_limit.content_creation_attempts >= CONTENT_CREATION_LIMIT:
                return jsonify({'message': 'Content creation limit reached. Try again later.'}), 429
            else:
                rate_limit.content_creation_attempts += 1
        else:
            rate_limit.content_creation_attempts = 1  # Reset count after 1 hour
            rate_limit.last_content_creation_attempt = datetime.now()

    db.session.commit()
    return jsonify({'message': 'Content created successfully.'}), 200