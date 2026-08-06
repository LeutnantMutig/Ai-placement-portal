# AI-Powered Placement Portal

An AI-powered Placement Portal developed using Django that connects Students, Employers, and Administrators on a single platform.

The system helps students create profiles, upload resumes, apply for jobs, and receive placement updates, while employers can manage job postings and applicants efficiently.  
The Admin Panel allows complete management and monitoring of the platform.


# 🚀 Features

## 👨‍🎓 Student Features

- Student Registration & Login
- Secure Authentication System
- Student Profile Management
- Resume Upload Functionality
- Skill Management
- AI-Based Skill Analysis
- Job Application System
- Personalized Dashboard
- Password Reset System
- Email Notifications


## 🏢 Employer Features

- Employer Registration & Login
- Company Profile Management
- Job Posting System
- Applicant Management
- Candidate Shortlisting
- Recruiter Dashboard
- Candidate Communication via Email


## 👨‍💼 Admin Features

- Secure Admin Dashboard
- Student Management
- Employer Management
- Job Post Monitoring
- Resume & Application Management
- User Authentication Control
- Database Management
- Platform Monitoring
- Admin Account Creation Support


## 🤖 AI Features

- AI Skill Detection
- Resume Skill Analysis
- Embedding-Based Processing
- Smart Recommendation Features


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
- MySQL

## AI Integration
- AI Embedding Features


# 📂 Project Structure

```bash
ai-placement-portal/
│
├── accounts/                 # Student account management
├── media/                    # Uploaded resumes and media files
├── placement_project/        # Main Django project settings
├── portal/                   # Core placement portal functionality , templates/ # HTML templates
├── static/                   # CSS, JavaScript, Images
├── create_admin.py           # Admin account creation script
├── manage.py                 # Django project manager
├── requirements.txt          # Project dependencies
└── Start_AI_Placement.bat    # Windows startup script
```


# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/LeutnantMutig/ai-placement-portal.git
cd ai-placement-portal
```


## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```


## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Configure Environment Variables

Create a `.env` file and add:

```env
SECRET_KEY=your_secret_key
DEBUG=True
```


## 5️⃣ Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```


## 6️⃣ Create Admin Account

### Option 1

```bash
python create_admin.py
```

### Option 2

```bash
python manage.py createsuperuser
```


## 7️⃣ Run Development Server

```bash
python manage.py runserver
```

Open browser:

```bash
http://127.0.0.1:8000/
```


# 🔐 Security

- `.env` file is excluded from GitHub
- Sensitive credentials are protected
- Secret keys are not uploaded publicly



# 🧾 Requirements

Example dependencies:

```txt
Django
python-dotenv
google-generativeai
Pillow
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```


# 👨‍💻 Author

Developed by Chirag Pawar

GitHub: https://github.com/LeutnantMutig


## 📝 License

This project is licensed under the MIT License.
