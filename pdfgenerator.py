# pdf_generator.py
from xhtml2pdf import pisa
from flask import make_response
from io import BytesIO
import json


def generate_pdf(resume):
  html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Resume</title>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            h1 {{ color: #333; }}
            h2 {{ color: #555; }}
            .section {{ margin-bottom: 20px; }}
            .item {{ margin-bottom: 10px; }}
        </style>
    </head>
    <body>
        <h1>{resume.title}</h1>
        <div class="section">
            <h2>Objective</h2>
            <p>{resume.objective or 'N/A'}</p>
        </div>
        <div class="section">
            <h2>Work Experience</h2>
           { format_work_experience(resume.work_experience)}
        </div>
        <div class="section">
            <h2>Education</h2>
            { format_education(resume.education)}
        </div>
        <div class="section">
            <h2>Skills</h2>
           { format_skills(resume.skills)}
         </div>
         <div class="section">
             <h2>Generated Content</h2>
             <p>{resume.generated_content or 'N/A'}</p>
          </div>
    </body>
    </html>
  """

  pdf = BytesIO()
  pisa_status = pisa.CreatePDF(html_content, dest=pdf)

  if not pisa_status.err:
      pdf.seek(0)
      response = make_response(pdf.read())
      response.headers['Content-Type'] = 'application/pdf'
      response.headers['Content-Disposition'] = 'inline; filename="resume.pdf"'
      return response
  else:
       return "Error generating PDF"


def format_work_experience(work_experience):
  if not work_experience:
      return "<p>N/A</p>"

  html = ""
  if isinstance(work_experience, str): # handle stringified json
    work_experience = json.loads(work_experience)
    
  if isinstance(work_experience, list):
    for item in work_experience:
      html += f'<div class="item"><strong>{item.get("title")}</strong><br>'\
             f'{item.get("company")}<br>'\
             f'{item.get("start_date")} - {item.get("end_date")}<br>'\
             f'{item.get("description")}</div>'
  else: # if not a list then handle
      html = f'<div class="item"><strong>{work_experience.get("title")}</strong><br>'\
             f'{work_experience.get("company")}<br>'\
             f'{work_experience.get("start_date")} - {work_experience.get("end_date")}<br>'\
             f'{work_experience.get("description")}</div>'
  return html

def format_education(education):
  if not education:
      return "<p>N/A</p>"
  html = ""
  if isinstance(education, str): # handle stringified json
    education = json.loads(education)

  if isinstance(education, list):
    for item in education:
        html += f'<div class="item"><strong>{item.get("degree")}</strong><br>'\
                 f'{item.get("university")}<br>'\
                 f'{item.get("graduation_year")}</div>'
  else:
      html = f'<div class="item"><strong>{education.get("degree")}</strong><br>'\
                 f'{education.get("university")}<br>'\
                 f'{education.get("graduation_year")}</div>'

  return html

def format_skills(skills):
  if not skills:
    return "<p>N/A</p>"
  html = ""
  if isinstance(skills, str): # handle stringified json
        skills = json.loads(skills)
  if isinstance(skills, list):
    html += "<ul>"
    for item in skills:
        html += f'<li>{item}</li>'
    html += "</ul>"
  else: # is not a list then handle
    html = f'<p>{skills}</p>'
  return html