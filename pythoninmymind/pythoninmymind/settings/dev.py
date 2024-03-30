from .base import *
import os 
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*', ]


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'postgres',
        'PASSWORD': '1234567890',
        'NAME': 'pythoninmymind',
    }
}

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pythoninmymind.settings.dev')