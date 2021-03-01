"""
Django settings for SqBlog project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't6(g^opd&x_rs%3qdqjrd9zv4#*v^sj^3i+7c=$h2_=3pn=w2y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['sqblogg.azurewebsites.net' , 'https://sqblogg.azurewebsites.net']


# Application definition

INSTALLED_APPS = [
    'users.apps.UsersConfig',
    'blog.apps.BlogConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'ckeditor',
    'ckeditor_uploader',
    'social_django',
]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]


ROOT_URLCONF = 'SqBlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',  # <-- Here
                'social_django.context_processors.login_redirect',  # <-- Here
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)



WSGI_APPLICATION = 'SqBlog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'SqBlog',
#         'USER': 'postgres',
#         'PASSWORD': '8343',
#         'HOST': 'localhost',
#     }
# }












DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
#


STATIC_URL = '/static/'
STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'static')

]

STATIC_ROOT= os.path.join(BASE_DIR,'assets')
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')









# STATIC_URL = '/static/'
# STATICFILES_DIRS=[
#     os.path.join(BASE_DIR,'static')
#
# ]
#
# STATIC_ROOT= os.path.join(BASE_DIR,'assets')
#
#
#
# STATIC_URL = '/static/'
# MEDIA_ROOT= os.path.join(BASE_DIR , 'media')
# MEDIA_URL = '/media/'


CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL='blog-home'
# LOGIN_URL='login'
# LOGIN_URL = '/auth/login/google-oauth2/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = 'logout'

####################################
##  CKEDITOR CONFIGURATION ##
####################################

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}

###################################


SOCIAL_AUTH_FACEBOOK_KEY = '3374170972644241'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '03d5faa5fee183bd56d5c424c2f2d784'  # App Secret


# 216620334306-1mm2jr6713nh6lv00ickkodg0prc4145.apps.googleusercontent.com  google key

# 9onpxmjypan3DGaNn8Xmq8n0 client secret

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '216620334306-1mm2jr6713nh6lv00ickkodg0prc4145.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '9onpxmjypan3DGaNn8Xmq8n0'
