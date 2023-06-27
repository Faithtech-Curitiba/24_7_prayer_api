"""
Django settings for prayer project.

Generated using django-split-settings, dj-database-url and python-decouple
"""

from pathlib import Path

import decouple
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

config = decouple.AutoConfig(BASE_DIR)

SECRET_KEY = config("DJANGO_SECRET_KEY")
DEBUG = config("DJANGO_DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = config("DJANGO_ALLOWED_HOSTS", default="*", cast=decouple.Csv())
CORS_ALLOW_ALL_ORIGINS = True

AUTH_USER_MODEL = "prayer.User"

APPEND_SLASH = True

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_filters",
    "django_crontab",
    "prayer",
    "health_check",
    "health_check.db",
    'corsheaders',    
]

CRONJOBS = [
    ("0,30 * * * *", "prayer.cron.notifications.send_emails"),
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = "prayer.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "prayer.wsgi.application"

DATABASES = {"default": config("DJANGO_DATABASE_URL", cast=dj_database_url.parse)}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = False

LOCALE_PATHS = [
    BASE_DIR / "locale",
]


STATIC_URL = "/static/"
STATIC_ROOT = "/static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = "/static/media/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
