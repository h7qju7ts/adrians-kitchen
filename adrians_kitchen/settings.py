from pathlib import Path
import os
import dj_database_url

# ---------------------------------------------------------
# BASE DIRECTORY
# ---------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# Load local env.py (only exists locally)
if os.path.isfile(BASE_DIR / "env.py"):
    import env


# ---------------------------------------------------------
# SECURITY
# ---------------------------------------------------------
SECRET_KEY = os.environ.get("SECRET_KEY")

# DEBUG:
# - Local machine → DEVELOPMENT=True → DEBUG=True
# - Heroku         → DEVELOPMENT missing → DEBUG=False
DEBUG = os.environ.get("DEVELOPMENT") == "True"

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "kitchen-adrian-84c5bb99022c.herokuapp.com",
]
 

# ---------------------------------------------------------
# APPLICATIONS
# ---------------------------------------------------------
INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",

    # Cloudinary
    "cloudinary_storage",
    "cloudinary",

    # Allauth
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",

    # Your app
    "bookings",
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]


# ---------------------------------------------------------
# MIDDLEWARE
# ---------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # Required for Heroku static files
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # Allauth
    "allauth.account.middleware.AccountMiddleware",
]


# ---------------------------------------------------------
# TEMPLATES
# ---------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

ROOT_URLCONF = "adrians_kitchen.urls"
WSGI_APPLICATION = "adrians_kitchen.wsgi.application"


# ---------------------------------------------------------
# DATABASES
# ---------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Heroku DATABASE_URL
if "DATABASE_URL" in os.environ:
    DATABASES["default"] = dj_database_url.config(
        conn_max_age=600, ssl_require=True
    )


# ---------------------------------------------------------
# PASSWORD VALIDATION
# ---------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# ---------------------------------------------------------
# INTERNATIONALIZATION
# ---------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# ---------------------------------------------------------
# STATIC FILES
# ---------------------------------------------------------
STATIC_URL = "/static/"

# Your app static folder → bookings/static/bookings/*
STATICFILES_DIRS = [
    BASE_DIR / "bookings" / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# ---------------------------------------------------------
# MEDIA / CLOUDINARY
# ---------------------------------------------------------
MEDIA_URL = "/media/"
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

CLOUDINARY_URL = os.environ.get("CLOUDINARY_URL")


# ---------------------------------------------------------
# ALLAUTH SETTINGS
# ---------------------------------------------------------
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "username_email"

LOGIN_URL = "account_login"
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

ACCOUNT_FORMS = {
    "signup": "bookings.forms.CustomSignupForm",
}


# ---------------------------------------------------------
# EMAIL BACKEND
# ---------------------------------------------------------
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# ---------------------------------------------------------
# MESSAGES (DISABLE LOGIN/LOGOUT NOTICES)
# ---------------------------------------------------------
MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

# Disable ALL auto messages from Allauth
ACCOUNT_LOGOUT_MESSAGE = False
ACCOUNT_LOGIN_ON_PASSWORD_RESET = False
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = False
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "/"
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "/"


# ---------------------------------------------------------
# DEFAULT FIELD TYPE
# ---------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
