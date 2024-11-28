"""
Module: config.settings

This module contains the settings for the Django project.
"""

import os
import sys
from pathlib import Path

from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (
    "django-insecure-$z3_q#$_c@$uawk-hs2_&0&8syy6%0^2@##7#$856pghqibnzu"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    # Third-party apps
    "django_translation_flags",  # Enhances translation with language flags
    "modeltranslation",  # Provides support for model field translation
    "drf_spectacular",  # OpenAPI schema generator
    "corsheaders",  # cors
    # Django built-in apps
    "django.contrib.admin",  # Django administration panel
    "django.contrib.auth",  # Django authentication system
    "django.contrib.contenttypes",  # Django content types framework
    "django.contrib.sessions",  # Django session framework
    "django.contrib.messages",  # Django messaging framework
    "django.contrib.staticfiles",  # Django static files framework
    # Custom apps
    "core.apps.CoreConfig",  # Core functionality app
    "users.apps.UsersConfig",  # User management app
]

MIDDLEWARE = [
    # Provides security features, such as setting security-related headers
    "django.middleware.security.SecurityMiddleware",
    # Manages sessions across requests
    "django.contrib.sessions.middleware.SessionMiddleware",
    # Handles user language preferences for dynamic language switching
    "django.middleware.locale.LocaleMiddleware",
    # Handles common operations for processing each request
    "django.middleware.common.CommonMiddleware",
    # Adds CSRF protection to views that use the CSRF token
    "django.middleware.csrf.CsrfViewMiddleware",
    # cors middleware
    "corsheaders.middleware.CorsMiddleware",
    # Handles user authentication
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    # Manages messages (e.g., from the messages framework)
    "django.contrib.messages.middleware.MessageMiddleware",
    # Adds the X-Frame-Options header to protect against clickjacking attacks
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # List of directories where the engine should look for template files.
        "DIRS": [BASE_DIR / "templates"],
        # Whether to look for templates in Django apps. If True,
        # DjangoTemplates looks for templates in a 'templates' subdirectory of
        # each app specified in INSTALLED_APPS.
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                #  Adds some variables to the context in debug mode.
                "django.template.context_processors.debug",
                #  Adds the request variable to the context.
                "django.template.context_processors.request",
                #  Adds the user and request variables to the context.
                "django.contrib.auth.context_processors.auth",
                #  Adds the messages variable to the context.
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        # Validates that the password is not too similar to the provided
        # user attributes
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa # pylint: disable=line-too-long
    },
    {
        # Validates that the password meets the minimum length requirement
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa # pylint: disable=line-too-long
    },
    {
        # Validates that the password is not a common password
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa # pylint: disable=line-too-long
    },
    {
        # Validates that the password contains at least one digit
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa # pylint: disable=line-too-long
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

# Specifies the default language for the application
LANGUAGE_CODE = "en"
# Specifies the default time zone for the application
TIME_ZONE = "Europe/Berlin"
# Enables translation of user-visible strings
USE_I18N = True
# Formats dates, numbers, and calendars according to the user's locale
USE_L10N = True
# Enables timezone support
USE_TZ = True

LOCALE_PATHS = (BASE_DIR / "locale",)


def gettext(s):
    """
    A function used for providing translations in the specified languages.

    Args:
        s (str): The input string to be translated.

    Returns:
        str: The translated string.
    """
    return s


# Define the supported languages for translation
LANGUAGES = [
    ("de", gettext(_("German"))),
    ("en", gettext(_("English"))),
]
DEFAULT_LANGUAGE = "en/"

# Set the default language for model translation
MODELTRANSLATION_DEFAULT_LANGUAGE = "en"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# The absolute path to the directory where collectstatic will collect static
# files for deployment.
STATIC_ROOT = BASE_DIR / "static"

# The base URL to serve static files from
STATIC_URL = "/static/"

# The absolute filesystem path to the directory that will hold
# user-uploaded files.
MEDIA_ROOT = BASE_DIR / "media"

# The base URL to serve user-uploaded media files from
MEDIA_URL = "/media/"

STATICFILES_DIRS = [
    BASE_DIR / "config/static",
    # Additional locations of static files
]

# Specifies a custom user model for authentication.
AUTH_USER_MODEL = "users.CustomUser"
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# appends apps to BASE_DIR path: ! should stay at the bottom of the file !
sys.path.append(os.path.join(BASE_DIR, "apps"))
