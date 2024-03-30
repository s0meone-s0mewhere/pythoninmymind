import os
from .base import *


DEBUG = False

ADMINS = [
    ('Artem Emelyanov', 'artememelyanov@icloud.com'),
]

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}

#CSRF_COOKIE_SECURE = True
#SESSION_COOKIE_SECURE = True
#SECURE_SSL_REDIRECT = True
