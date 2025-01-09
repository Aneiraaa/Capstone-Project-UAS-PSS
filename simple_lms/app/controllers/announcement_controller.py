from flask import request, jsonify
from .. import db
from ..models import Announcement

def create_announcement(course_id):
    data = request.get_json()
    new_announcement = Announcement(
        course_id=course_id,
        content=data['content'],
        date=data['date']
    )
    db.session.add(new_announcement)
    db.session.commit()
    return jsonify({'message': 'Announcement created successfully', 'announcement_id': new_announcement.id}), 201

def show_announcements(course_id):
    announcements = Announcement.query.filter_by(course_id=course_id).all()
    return jsonify([{
        'id': announcement.id,
        'content': announcement.content,
        'date': announcement.date
    } for announcement in announcements]), 200

def edit_announcement(announcement_id):
    announcement = Announcement.query.get(announcement_id)
    if announcement is None:
        return jsonify({'message': 'Announcement not found'}), 404

    data = request.get_json()
    announcement.content = data.get('content', announcement.content)
    announcement.date = data.get('date', announcement.date)

    db.session.commit()
    return jsonify({'message': 'Announcement updated successfully'}), 200

def delete_announcement(announcement_id):
    announcement = Announcement.query.get(announcement_id)
    if announcement is None:
        return jsonify({'message': 'Announcement not found'}), 404

    db.session.delete(announcement)
    db.session.commit()
    return jsonify({'message': 'Announcement deleted successfully'}), 200