"""
Django settings for adrians_kitchen project.

This file contains all configuration for your Django project:
- Installed apps
- Middleware
- Templates
- Authentication
- Static files
- Allauth settings
- Database
"""

from pathlib import Path
import os

# -------------------------------------------------------------------------
# BASE DIRECTORY
# -------------------------------------------------------------------------
# BASE_DIR is used to build paths inside the project.
# Example: BASE_DIR / 'templates' → "your_project/templates/"
BASE_DIR = Path(__file__).resolve().parent.parent


# -------------------------------------------------------------------------
# SECURITY SETTINGS
# -------------------------------------------------------------------------

# Secret key used for hashing passwords, sessions, CSRF, etc.
# ⚠️ IMPORTANT: Never commit this key publicly in real production.
SECRET_KEY = 'django-insecure-(+(gb7nis48j@6(90*t_wwh7qv6$i(j5*v-f7w=6(jdi+r22y%'

# Debug mode:
# - True: for development (shows detailed errors)
# - False: for production (hides errors from users)
DEBUG = False

# Your allowed domains:
# Django will only respond to requests coming from these addresses.
ALLOWED_HOSTS = [
    'kitchen-adrian-84c5bb99022c.herokuapp.com',
    '127.0.0.1',
]


# -------------------------------------------------------------------------
# INSTALLED APPS
# -------------------------------------------------------------------------
# These are all the apps your Django project uses.
# Django's default apps + Allauth + your "bookings" app.

INSTALLED_APPS = [
    # Django core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Required for Django Allauth
    'django.contrib.sites',

    # Allauth apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # Your custom booking app
    'bookings',
]


# -------------------------------------------------------------------------
# MIDDLEWARE
# -------------------------------------------------------------------------
# Middleware is like layers that process each request.
# Example: security, sessions, authentication, CSRF protection, etc.

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # Whitenoise allows Django to serve static files on Heroku
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',

    # Handles logged-in users
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Required for Django Allauth
    'allauth.account.middleware.AccountMiddleware',
]


# -------------------------------------------------------------------------
# URL CONFIGURATION
# -------------------------------------------------------------------------
ROOT_URLCONF = 'adrians_kitchen.urls'


# -------------------------------------------------------------------------
# TEMPLATES
# -------------------------------------------------------------------------
# Django will look for templates in:
# 1. BASE_DIR / "templates"
# 2. templates/ folders inside apps (APP_DIRS=True)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # The main place where global templates (like allauth) sit
        'DIRS': [BASE_DIR / "templates"],

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'adrians_kitchen.wsgi.application'


# -------------------------------------------------------------------------
# DATABASE
# -------------------------------------------------------------------------
# SQLite is good for development.
# On Heroku, the DATABASE_URL config will replace this automatically.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# -------------------------------------------------------------------------
# PASSWORD VALIDATION
# -------------------------------------------------------------------------
# Django’s recommended password strength checks.

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# -------------------------------------------------------------------------
# INTERNATIONALIZATION
# -------------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# -------------------------------------------------------------------------
# STATIC FILES
# -------------------------------------------------------------------------
# Static files = CSS, JS, images.

STATIC_URL = '/static/'

# Where your CSS lives inside the app:
STATICFILES_DIRS = [
    BASE_DIR / 'bookings' / 'static'
]

# Where Django collects all static files for production
STATIC_ROOT = BASE_DIR / 'staticfiles'

# For Heroku (Whitenoise)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# -------------------------------------------------------------------------
# DEFAULT PRIMARY KEY
# -------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# -------------------------------------------------------------------------
# LOGIN / LOGOUT SETTINGS
# -------------------------------------------------------------------------
# Where users go after login/logout
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'


# -------------------------------------------------------------------------
# DJANGO ALLAUTH CONFIGURATION
# -------------------------------------------------------------------------

# Required for Allauth
SITE_ID = 1

# Authentication backends:
# - Django's normal login
# - Allauth login system
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Allauth behavior settings
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'   # Login using username OR email
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'            # Options: 'mandatory', 'optional', 'none'
ACCOUNT_USERNAME_REQUIRED = True
