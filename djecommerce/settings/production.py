from .base import *

DEBUG = False
ALLOWED_HOSTS = ['shop-app-django.herokuapp.com']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd24se35lcq78vc',
        'USER': 'mkbdtuxrmwglsr',
        'PASSWORD': '36e6d7fa32c2305ee7cd8c5a6bddcbf6e0c803e29ba4df289acd4242bbbb08d6',
        'HOST': 'ec2-3-228-114-251.compute-1.amazonaws.com',
        'PORT': '5432'
    }
}


STRIPE_PUBLIC_KEY = 'your-live-public-key'
STRIPE_SECRET_KEY = 'your-live-secret-key'

