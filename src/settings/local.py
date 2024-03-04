from .base import *

ALLOWED_HOSTS = config("ALLOWED_HOSTS").split()

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'local.sqlite3',
    }
}