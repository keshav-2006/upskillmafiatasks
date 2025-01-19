# resume_manager.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Resume
from database import db
from gemini import generate_resume_content # type: ignore # Assuming gemini.py has generate_resume_content function
from pdf_generator import generate_pdf # Assuming pdf_generator.py has generate_pdf function


resume_bp = Blueprint('resume', __name__)

@resume_bp.route('/', methods=['POST'])
@jwt_required()
def create_resume():
    current_user_id = get_jwt_identity()
    data = request.get_json()
    if not data.get('title'):
        return jsonify({"message":"title is required."}), 400
    new_resume = Resume(user_id=current_user_id, title=data['title'])
    db.session.add(new_resume)
    db.session.commit()
    return jsonify({'message':'Resume draft created successfully', 'resume_id':new_resume.id}), 201

@resume_bp.route('/', methods=['GET'])
@jwt_required()
def get_user_resumes():
    current_user_id = get_jwt_identity()
    resumes = Resume.query.filter_by(user_id=current_user_id).all()
    resumes_list = []
    for resume in resumes:
        resumes_list.append({
            "id": resume.id,
            "title": resume.title,
            "objective": resume.objective,
            "created_at": resume.created_at,
            "updated_at": resume.updated_at
        })
    return jsonify(resumes_list), 200


@resume_bp.route('/<int:resume_id>', methods=['GET'])
@jwt_required()
def get_resume(resume_id):
    current_user_id = get_jwt_identity()
    resume = Resume.query.filter_by(id=resume_id, user_id=current_user_id).first()
    if resume:
        return jsonify({
            "id": resume.id,
            "title": resume.title,
            "objective": resume.objective,
            "work_experience": resume.work_experience,
            "education": resume.education,
            "skills": resume.skills,
            "generated_content": resume.generated_content,
            "created_at": resume.created_at,
            "updated_at": resume.updated_at
        }), 200
    return jsonify({'message': 'Resume not found'}), 404

@resume_bp.route('/<int:resume_id>', methods=['PUT'])
@jwt_required()
def update_resume(resume_id):
    current_user_id = get_jwt_identity()
    resume = Resume.query.filter_by(id=resume_id, user_id=current_user_id).first()
    if not resume:
        return jsonify({'message': 'Resume not found'}), 404

    data = request.get_json()
    resume.title = data.get('title', resume.title)
    resume.objective = data.get('objective', resume.objective)
    resume.work_experience = data.get('work_experience', resume.work_experience)
    resume.education = data.get('education', resume.education)
    resume.skills = data.get('skills', resume.skills)
    db.session.commit()

    return jsonify({'message': 'Resume updated successfully'}), 200

@resume_bp.route('/<int:resume_id>', methods=['DELETE'])
@jwt_required()
def delete_resume(resume_id):
    current_user_id = get_jwt_identity()
    resume = Resume.query.filter_by(id=resume_id, user_id=current_user_id).first()
    if not resume:
        return jsonify({'message': 'Resume not found'}), 404
    db.session.delete(resume)
    db.session.commit()
    return jsonify({'message': 'Resume deleted successfully'}), 200

@resume_bp.route('/<int:resume_id>/generate', methods=['POST'])
@jwt_required()
def generate_content(resume_id):
     current_user_id = get_jwt_identity()
     resume = Resume.query.filter_by(id=resume_id, user_id=current_user_id).first()
     if not resume:
        return jsonify({'message': 'Resume not found'}), 404
    
     generated_content = generate_resume_content(resume)
     resume.generated_content = generated_content
     db.session.commit()
     return jsonify({'message': 'Resume content generated successfully'}), 200
 
@resume_bp.route('/<int:resume_id>/download', methods=['GET'])
@jwt_required()
def download_resume(resume_id):
    current_user_id = get_jwt_identity()
    resume = Resume.query.filter_by(id=resume_id, user_id=current_user_id).first()
    if not resume:
         return jsonify({'message': 'Resume not found'}), 404
    
    pdf_file = generate_pdf(resume)
    return pdf_file