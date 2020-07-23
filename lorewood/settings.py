"""
Django settings for lorewood project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i_6_gq)3)iq-m#(sync@yp$oq87u31rp+z9dr93qw8gtcuzjk5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['lorewood.online', 'localhost', '127.0.0.1', 'www.lorewood.online']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'el_pagination',
    'social_django',
    'app.apps.AppConfig',
    'rest_framework',
    'django_wysiwyg',
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'lorewood.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'lorewood.wsgi.application'
DJANGO_WYSIWYG_FLAVOR = "ckeditor"

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LOGIN_REDIRECT_URL = "/"


# Authentication Backends
AUTHENTICATION_BACKENDS = [
    'social_core.backends.vk.VKOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
    'django.contrib.auth.backends.AllowAllUsersModelBackend'
]

SOCIAL_AUTH_POSTGRES_JSONFIELD = True

SOCIAL_AUTH_VK_OAUTH2_KEY = '7033607'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'mHZ6n0XvxVY2nU1iz9Xy'

SOCIAL_AUTH_FACEBOOK_KEY = '2337877396434591'
SOCIAL_AUTH_FACEBOOK_SECRET = 'dc47e6dec09c54a09c09e0f37125c982'

SOCIAL_AUTH_TWITTER_KEY = 'PiNRffwXtKcCQQ8udFsdQmVOG'
SOCIAL_AUTH_TWITTER_SECRET = 'fFinacLTmcubfSL7exgDY7oS7SweyFAJI8KnYc8sUqUaPUNEZG'

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/
from django.utils.translation import ugettext_lazy as _

LANGUAGES = (
    ('en', _('English')),
    ('ru', _('Russian')),
)

LANGUAGE_CODE = 'ru'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'app/locale'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/media/"

CKEDITOR_UPLOAD_PATH = 'uploads'

# Mail server data
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'lorewood.info@gmail.com'
EMAIL_HOST_PASSWORD = 'lorewood.info.password'
EMAIL_PORT = 587

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'file': {
            'format': '{asctime} - [{levelname}]: {funcName} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'lorewood.log',
            'formatter': 'file'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        },
        'app': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# Activate Django-Heroku.
import django_heroku

django_heroku.settings(locals())
