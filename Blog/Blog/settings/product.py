#!/user/bin/env python
# 每天都要有好心情
from .base import *  # NOQA

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_db',
        'USER': 'root',
        'PASSWORD': 'T85568397',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'CONN_MAX_AGE': 5 * 60,
        'OPTIONS': {
            'charset': 'utf8mb4',
        }
    }
}

REDIS_URL = 'redis://127.0.0.1:6379/1'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'TIMEOUT': 300,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
        },
        'CONNECTION_POOL_CLASS': 'redis.connection.BlockingConnectionPool',
    }
}

INSTALLED_APPS += [
    'silk',
]

MIDDLEWARE += [
    'silk.middleware.SilkyMiddleware',
]
