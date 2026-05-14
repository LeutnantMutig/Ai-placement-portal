# AI-Powered Placement Portal

A full-stack AI-powered Placement Portal developed using Django that connects Students and Employers on a single platform.  
The system allows students to create profiles, upload resumes, and apply for jobs, while employers can post opportunities and manage applicants efficiently.



# 🚀 Features

## 👨‍🎓 Student Features

- Student Registration & Login
- Profile Management
- Resume Upload
- Skill Management
- AI-Based Skill Analysis
- Job Application System
- Dashboard Access
- Email Notifications



## 🏢 Employer Features

- Employer Registration & Login
- Company Profile Management
- Job Posting System
- Applicant Management
- Candidate Shortlisting
- Recruiter Dashboard
- Candidate Communication via Email



## 🤖 AI Features

- AI Skill Detection
- Resume Skill Analysis
- Embedding-Based Processing
- Smart Recommendations



# 🛠️ Tech Stack

## Frontend
- HTML
- CSS
- Bootstrap
- JavaScript

## Backend
- Python
- Django

## Database
- SQLite

## AI Integration
- Gemini API
- AI Embedding Features



# 📂 Project Structure

```bash
placement_project/
│
├── accounts/
├── employers/
├── templates/
├── static/
├── media/
├── placement_project/
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore

⚙️ Installation Guide
1️⃣ Clone Repository
  git clone https://github.com/YOUR_USERNAME/placement-portal.git
  cd placement-portal

2️⃣ Create Virtual Environment
  python -m venv venv
  Activate Environment
  
  Windows
  venv\Scripts\activate
  
  Linux / Mac
  source venv/bin/activate

3️⃣ Install Dependencies
  pip install -r requirements.txt

4️⃣ Configure Environment Variables
  Create .env file:
  SECRET_KEY=your_secret_key
  DEBUG=True

5️⃣ Run Database Migrations
  python manage.py makemigrations
  python manage.py migrate

6️⃣ Run Development Server
  python manage.py runserver

  Open browser:
  http://127.0.0.1:8000/
