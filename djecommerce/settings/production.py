from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dcdtcaiahit70v',
        'USER': 'yrfkxmcsoviljl',
        'PASSWORD': '34ff47a94a83fd334399c828e6531f70326cebc1c122e69e95c5bb8bd07b1bec',
        'HOST': 'ec2-3-233-236-188.compute-1.amazonaws.com',
        'PORT': '5432'
    }
}


STRIPE_PUBLIC_KEY = 'your-live-public-key'
STRIPE_SECRET_KEY = 'your-live-secret-key'

