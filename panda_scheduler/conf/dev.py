from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'panda-scheduler',
        'USER': 'moritzkrog',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
