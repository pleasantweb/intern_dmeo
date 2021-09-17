from .base import *
from decouple import config
DEBUG = True
ALLOWED_HOSTS = []
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': config('MYSQL_DATABASE_NAME'),
            'USER': config('MYSQL_DATABASE_USER'),
            'PASSWORD': config('MYSQL_DATABASE_PASSWORD'),
            'HOST': config('MYSQL_DATABASE_HOST'),
            'PORT': config('MYSQL_DATABASE_PORT'),
        }
    }
