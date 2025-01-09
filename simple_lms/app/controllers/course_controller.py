from flask import request, jsonify
from .. import db
from ..models import Course, Enrollment

def batch_enroll(course_id):
    data = request.get_json()
    
    # Fetch the course to check the enrollment limit
    course = Course.query.get(course_id)
    if not course:
        return jsonify({'message': 'Course not found'}), 404

    # Check the maximum enrollment limit set by the teacher
    max_students = course.max_students  # Assuming you have a max_students field in your Course model
    current_enrollment_count = Enrollment.query.filter_by(course_id=course_id).count()

    # Check if the course is already full
    if current_enrollment_count >= max_students:
        return jsonify({'message': 'Enrollment limit reached. No more students can be enrolled.'}), 400

    # Enroll students
    enrolled_students = []
    for student_id in data['student_ids']:
        # Check if the student is already enrolled
        existing_enrollment = Enrollment.query.filter_by(user_id=student_id, course_id=course_id).first()
        if existing_enrollment:
            return jsonify({'message': f'Student {student_id} is already enrolled in this course.'}), 400
        
        # Create a new enrollment
        enrollment = Enrollment(user_id=student_id, course_id=course_id)
        db.session.add(enrollment)
        enrolled_students.append(student_id)

    db.session.commit()
    
    return jsonify({'message': 'Students enrolled successfully', 'enrolled_students': enrolled_students}), 200

def create_course():
    data = request.get_json()
    new_course = Course(
        title=data['title'],
        description=data.get('description')
    )
    db.session.add(new_course)
    db.session.commit()
    return jsonify({'message': 'Course created successfully', 'course_id': new_course.id}), 201