"""
Django settings for vsdk project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
#from . import custom_storages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tk2(l(00&kfe7j97j$dvgz&b6r!kk_zbse1(9w*eoc$bcwu773'

# SECURITY WARNING: don't run with debug turned on in production!

##########
#Use True on your local PC, False on Heroku!!
########
#DEBUG = True
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'vsdk.service_development.apps.ServiceDevelopmentConfig',
    'storages',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #TODO: disabled csrf middleware, is this usable with voiceXML?
    #    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vsdk.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'vsdk.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
if DEBUG:
     DATABASES = {
             'default': {
                         'ENGINE': 'django.db.backends.sqlite3',
                         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                     }
          }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'this is not a correct database',
            'USER': 'this is not a corret user',
            'PASSWORD': 'this is not a correct password (probably)',
            'HOST': 'localhost',
            'PORT':'',
        }
    }
    import dj_database_url
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Amsterdam'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
STATIC_ROOT = os.path.join(SITE_ROOT, 'staticfiles')
STATICFILES_DIRS = (
  os.path.join(SITE_ROOT, 'static/'),
  os.path.join(SITE_ROOT, 'uploads/'),
)

MEDIA_ROOT = os.path.join(SITE_ROOT, 'uploads')
MEDIA_URL = '/uploads/'


# Update database configuration with $DATABASE_URL.ALLOWED_HOSTSimport
# dj_database_url




# Simplified static file serving.ALLOWED_HOSTS#
# https://warehouse.python.org/project/whitenoise/
try:
    FTP_PASS =  os.environ['FTP_PASS']
    FTP_DIR = os.environ['FTP_DIR']
except KeyError:
    FTP_PASS = ""
    FTP_DIR = ""
FTP_STORAGE_LOCATION = 'ftp://ict4d:' + FTP_PASS + '@ict4d-vps.andrebaart.nl:21/'+ FTP_DIR +'/'
STATICFILES_LOCATION = FTP_STORAGE_LOCATION + '/static/'
MEDIAFILES_LOCATION = FTP_STORAGE_LOCATION + '/media/'
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

if not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
    STATIC_URL = "http://ict4d-vps.andrebaart.nl:2017/django-static/django-files/static/"
    MEDIA_URL = "http://ict4d-vps.andrebaart.nl:2017/django-static/django-files/"

    STATICFILES_STORAGE = 'vsdk.custom_storages.StaticStorage'
    DEFAULT_FILE_STORAGE ='vsdk.custom_storages.MediaStorage'


