from pathlib import Path
import os
import dj_database_url

# ---------------------------------------------------------
# BASE DIR
# ---------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# Load env.py if it exists
if os.path.isfile(os.path.join(BASE_DIR, "env.py")):
    import env

# ---------------------------------------------------------
# SECURITY
# ---------------------------------------------------------
SECRET_KEY = os.environ.get("SECRET_KEY")

# DEBUG:
#   Locally → DEVELOPMENT=True → DEBUG=True
#   Heroku  → DEVELOPMENT missing → DEBUG=False
DEBUG = os.environ.get("DEVELOPMENT") == "True"

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "kitchen-adrian-84c5bb99022c.herokuapp.com",
]

# ---------------------------------------------------------
# APPLICATION DEFINITION
# ---------------------------------------------------------
INSTALLED_APPS = [
    # Django core
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

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

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # Whitenoise for static on Heroku
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

ROOT_URLCONF = "adrians_kitchen.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # allauth + custom templates
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

WSGI_APPLICATION = "adrians_kitchen.wsgi.application"

# ---------------------------------------------------------
# DATABASES
# ---------------------------------------------------------
# Local = SQLite
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Heroku = Uses DATABASE_URL
if "DATABASE_URL" in os.environ:
    DATABASES["default"] = dj_database_url.config(conn_max_age=600, ssl_require=True)

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
# STATIC FILES (CSS/JS)
# ---------------------------------------------------------
STATIC_URL = "/static/"

# Your app's CSS/JS/images folder
# → bookings/static/bookings/*
STATICFILES_DIRS = [
    BASE_DIR / "bookings" / "static" / "bookings"
]

STATIC_ROOT = BASE_DIR / "staticfiles"

# Whitenoise for Heroku static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ---------------------------------------------------------
# MEDIA (Images uploaded by the user)
# ---------------------------------------------------------
MEDIA_URL = "/media/"

# Cloudinary for all media uploads
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

# ---------------------------------------------------------
# CLOUDINARY
# ---------------------------------------------------------
CLOUDINARY_URL = os.environ.get("CLOUDINARY_URL")

# ---------------------------------------------------------
# LOGIN SETTINGS
# ---------------------------------------------------------
LOGIN_URL = "account_login"
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

# ---------------------------------------------------------
# ALLAUTH SETTINGS
# ---------------------------------------------------------
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "username_email"

ACCOUNT_FORMS = {
    "signup": "bookings.forms.CustomSignupForm",
}

# Email backend (console for dev)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"