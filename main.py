# main.py
from flask import Flask, request, jsonify
from auth import auth_bp
from resume_manager import resume_bp
from database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost:5432/resume_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(auth_bp, url_prefix='/users')
app.register_blueprint(resume_bp, url_prefix='/resumes')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)