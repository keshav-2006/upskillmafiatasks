# gemini.py
from google.generativeai import GenerativeModel
import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

def generate_resume_content(resume):
  gemini_api_key = os.getenv("GEMINI_API_KEY")
  model = GenerativeModel('gemini-pro', api_key=gemini_api_key)

  prompt = f"Generate resume content for a resume with following details: \
          title: {resume.title}. \
          objective: {resume.objective}. \
          work_experience: {resume.work_experience}. \
          education: {resume.education}. \
          skills: {resume.skills}. "
    
  response = model.generate_content(prompt)
  return response.text #or you can parse and structured if needed