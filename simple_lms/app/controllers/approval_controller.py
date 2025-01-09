from flask import request, jsonify
from .. import db
from ..models import Content

def update_content(content_id):
    content = Content.query.get(content_id)
    if content is None:
        return jsonify({'message': 'Content not found'}), 404

    data = request.get_json()
    content.title = data.get('title', content.title)
    content.body = data.get('body', content.body)

    db.session.commit()
    return jsonify({'message': 'Content updated successfully'}), 200

def publish_content(content_id):
    content = Content.query.get(content_id)
    if content is None:
        return jsonify({'message': 'Content not found'}), 404

    content.published = True
    db.session.commit()
    return jsonify({'message': 'Content published successfully'}), 200

def unpublish_content(content_id):
    content = Content.query.get(content_id)
    if content is None:
        return jsonify({'message': 'Content not found'}), 404

    content.published = False
    db.session.commit()
    return jsonify({'message': 'Content unpublished successfully'}), 200