from .base import *

ALLOWED_HOSTS = ['*']

DEBUG = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        "main_format": {
            "format": "{asctime} - {levelname} - {module} - {filename} - {message}",
            "style": "{",
        }
    },
    'handlers': {
        'console': {
            "class": "logging.StreamHandler",
            "formatter": "main_format"
        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "main_format",
            "filename": "logs.log"
            }
        },
    'loggers': {
        'main': {
            "handlers": ["console", "file"],
            'level': 'INFO',
            'propagate': True
            }
        }
    }



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'local.sqlite3',
    }
}