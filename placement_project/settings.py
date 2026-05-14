# from pathlib import Path
# import os
# from dotenv import load_dotenv
# from django.core.exceptions import ImproperlyConfigured
# import pymysql
# pymysql.install_as_MySQLdb()


# BASE_DIR = Path(__file__).resolve().parent.parent
# load_dotenv(BASE_DIR / '.env')

# def get_secret(setting):
#     try:
#         return os.environ[setting]
#     except KeyError:
#         raise ImproperlyConfigured(f"Set the {setting} environment variable")

# # SECRET_KEY - No default in production to avoid insecure keys
# if 'DJANGO_SECRET_KEY' in os.environ:
#     SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
# else:
#     if os.environ.get('DEBUG', 'True').lower() == 'true':
#         SECRET_KEY = 'django-insecure-1234567890abcdef'  # dev only
#     else:
#         raise ImproperlyConfigured("DJANGO_SECRET_KEY not set in production")

# DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'

# # ALLOWED_HOSTS - allow '*' in DEBUG, otherwise parse list
# if DEBUG:
#     ALLOWED_HOSTS = ['*']
# else:
#     ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',  # <--- add this line
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'django_crontab',
#     'accounts',
#     'portal',
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',  # Must come before auth middleware
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',  # Must be after sessions
#     'django.contrib.messages.middleware.MessageMiddleware',    # Must be after auth
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]


# ROOT_URLCONF = 'placement_project.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [BASE_DIR / 'templates'],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'placement_project.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'placement_db',      # your database name
#         'USER': 'root',              # your MySQL username
#         'PASSWORD': 'yourpassword',  # your MySQL password
#         'HOST': 'localhost',         # or IP if remote
#         'PORT': '3306',              # default MySQL port
#         'OPTIONS': {
#             'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
#         },
#     }
# }


# AUTH_USER_MODEL = 'accounts.CustomUser'

# AUTH_PASSWORD_VALIDATORS = [
#     # your validators here...
# ]

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / 'static']
# STATIC_ROOT = BASE_DIR / 'staticfiles'

# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LOGIN_URL = '/login/'
# LOGIN_REDIRECT_URL = '/dashboard/'
# LOGOUT_REDIRECT_URL = '/'

# from django.contrib.messages import constants as messages
# MESSAGE_TAGS = {
#     messages.DEBUG: 'alert-info',
#     messages.INFO: 'alert-info',
#     messages.SUCCESS: 'alert-success',
#     messages.WARNING: 'alert-warning',
#     messages.ERROR: 'alert-danger',
# }

# # Email Configuration
# EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')
# if EMAIL_BACKEND:
#     # If explicitly set
#     if 'smtp' in EMAIL_BACKEND.lower():
#         EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
#         EMAIL_PORT = int(os.environ.get('EMAIL_PORT', '587'))
#         EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True').lower() == 'true'
#         EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
#         EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
#         DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER or 'no-reply@example.com')
# else:
#     if DEBUG:
#         # Dev mode: print emails to console
#         EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#         DEFAULT_FROM_EMAIL = 'no-reply@example.com'
#     else:
#         # Prod defaults (must be configured in env)
#         EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#         EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
#         EMAIL_PORT = int(os.environ.get('EMAIL_PORT', '587'))
#         EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True').lower() == 'true'
#         EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
#         EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
#         DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER or 'no-reply@example.com')


# # Run the task every day at 8:00 AM server time
# CRONJOBS = [
#     ('0 8 * * *', 'portal.cron.send_today_interview_reminders_job')
# ]




from pathlib import Path
import os
from dotenv import load_dotenv
from django.core.exceptions import ImproperlyConfigured
import pymysql

# Ensure MySQL driver works with Django
pymysql.install_as_MySQLdb()

# ---------------------------------------------------------
# BASE & ENV SETUP
# ---------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')


def get_secret(setting):
    """Helper to get environment variables safely"""
    try:
        return os.environ[setting]
    except KeyError:
        raise ImproperlyConfigured(f"Set the {setting} environment variable")


# ---------------------------------------------------------
# SECURITY SETTINGS
# ---------------------------------------------------------
if 'DJANGO_SECRET_KEY' in os.environ:
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
else:
    if os.environ.get('DEBUG', 'True').lower() == 'true':
        SECRET_KEY = 'django-insecure-1234567890abcdef'  # Dev only
    else:
        raise ImproperlyConfigured("DJANGO_SECRET_KEY not set in production")

DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')


# ---------------------------------------------------------
# INSTALLED APPS
# ---------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_crontab',
    'accounts',
    'portal',
    'widget_tweaks',
]


# ---------------------------------------------------------
# MIDDLEWARE
# ---------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ---------------------------------------------------------
# URLS / WSGI
# ---------------------------------------------------------
ROOT_URLCONF = 'placement_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'placement_project.wsgi.application'


# ---------------------------------------------------------
# DATABASE (MYSQL CONFIG)
# ---------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'placement_db',   # ✅ your new DB name
        'USER': 'root',           # ✅ your existing MySQL username
        'PASSWORD': 'Robi@123',   # ✅ your existing password
        'HOST': 'localhost',
        'PORT': '3306',
    }
}



# ---------------------------------------------------------
# AUTH / USER MODEL
# ---------------------------------------------------------
AUTH_USER_MODEL = 'accounts.CustomUser'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ---------------------------------------------------------
# LANGUAGE & TIMEZONE
# ---------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# ---------------------------------------------------------
# STATIC & MEDIA FILES
# ---------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ---------------------------------------------------------
# LOGIN / LOGOUT REDIRECTS
# ---------------------------------------------------------
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'


# ---------------------------------------------------------
# MESSAGES (Bootstrap friendly)
# ---------------------------------------------------------
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}


# ---------------------------------------------------------
# DOMAIN CONFIGURATION (For password reset links)
# ---------------------------------------------------------
# For local development with mobile access, use your computer's IP address
# Find your IP: Windows: ipconfig, Linux/Mac: ifconfig
# Example: '192.168.1.100:8000' or 'yourdomain.com'
SITE_DOMAIN = os.environ.get('SITE_DOMAIN', '172.20.10.3:8000')  # Default to localhost
SITE_PROTOCOL = os.environ.get('SITE_PROTOCOL', 'http')  # Use 'https' in production

# ---------------------------------------------------------
# EMAIL CONFIGURATION
# ---------------------------------------------------------
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')

if EMAIL_BACKEND:
    # If explicitly set
    if 'smtp' in EMAIL_BACKEND.lower():
        EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
        EMAIL_PORT = int(os.environ.get('EMAIL_PORT', '587'))
        EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True').lower() == 'true'
        EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
        EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
        DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER or 'no-reply@example.com')
else:
    if DEBUG:
        EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
        DEFAULT_FROM_EMAIL = 'no-reply@example.com'
    else:
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
        EMAIL_PORT = int(os.environ.get('EMAIL_PORT', '587'))
        EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True').lower() == 'true'
        EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
        EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
        DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER or 'no-reply@example.com')


# ---------------------------------------------------------
# CRON JOBS (Daily interview reminders)
# ---------------------------------------------------------
CRONJOBS = [
    ('0 8 * * *', 'portal.cron.send_today_interview_reminders_job')
]

# ---------------------------------------------------------
# DEFAULT AUTO FIELD
# ---------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
