from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-x@g3w#btb4$#=xry=x!@=84wf5-8e70@yvoyjh+($g2kftbnw_'

DEBUG = True

ALLOWED_HOSTS = []

[]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'ckeditor',
    'ckeditor_uploader',
    'rest_framework',
    'webpush',
    'django.contrib.flatpages',
    'twilio'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

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

WSGI_APPLICATION = 'project.wsgi.application'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
        "ROUTING": "chat.routing.channel_routing",
        'CONFIG': {
                    # "hosts": [('127.0.0.1', 8000)],
                    "hosts": [CELERY_BROKER_URL]
                },
        },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

WEBPUSH_SETTINGS = {
    "VAPID_PUBLIC_KEY": "BPkfteyRfo89qR7Zb4Toq-sXHLCxePW1EDJdRK8oZ4BqLizGJKPd_fNVC-VwzXDkTFyCGpdgCCAHxPaaBzKS8c0",
    "VAPID_PRIVATE_KEY":"AnHojrgtRdesSWpKEZSR5VCEEGfV1VQRLtPKQP5B2eQ",
    "VAPID_ADMIN_EMAIL": "testoviymailsf@gmail.com"
}

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

MEDIA_URL = '/static/'
STATIC_URL = '/static/'
STATIC_ROOT = 'app/static/'
MEDIA_ROOT = 'app/media/'
STATICFILES_DIRS = [BASE_DIR / 'static_src']

CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "ckeditor"

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'app/media')
