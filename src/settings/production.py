from .base import *

ALLOWED_HOSTS = config("ALLOWED_HOSTS").split()

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
    }
}