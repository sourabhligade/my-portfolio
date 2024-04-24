# Django settings for myportfolio project.

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'juv^rw+x=t(#v4q0#*-jd$+y!4&--ct544-76=+=zx2ls0#*md'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: Set a value for SECURE_HSTS_SECONDS
SECURE_HSTS_SECONDS = 31536000  # Example value for one year

# SECURITY WARNING: Set SECURE_SSL_REDIRECT to True
SECURE_SSL_REDIRECT = True

# SECURITY WARNING: Set SESSION_COOKIE_SECURE to True
SESSION_COOKIE_SECURE = True

# SECURITY WARNING: Set CSRF_COOKIE_SECURE to True
CSRF_COOKIE_SECURE = True

# SECURITY WARNING: Set ALLOWED_HOSTS to your domain(s)
ALLOWED_HOSTS = ['vercel.app', 'www.example.com', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'portfolio',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
'/Users/sourabhligade/myportfolio/portfolio/static']

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

ROOT_URLCONF = 'myportfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # Add the path to your project's template directory here
            '/Users/sourabhligade/myportfolio/portfolio/templates/portfolio',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myportfolio.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# Uncomment the following lines if not already included
# STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files (Uploaded files)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True