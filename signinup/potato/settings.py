import os
import json
import datetime
from pathlib import Path
from datetime import timedelta
from django.core.exceptions import ImproperlyConfigured
from django.contrib.messages import constants as messages_constants

MESSAGE_LEVEL = messages_constants.DEBUG
# /Users/etlaou/Downloads/Market/potato
BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = True
ALLOWED_HOSTS = []

#secret.json 파일에 외부로 노출해서는 안되는 정보를 입력해
#데이터를 보호한다
secret_file = os.path.join(BASE_DIR, './secret.json')
secrets = ''
with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secret=secrets):
    try:
        return secret[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_secret("DJANGO_SECRET_KEY")
COGNITO_AWS_REGION = get_secret("COGNITO_AWS_REGION")
COGNITO_USER_POOL = get_secret("COGNITO_USER_POOL")
COGNITO_AUDIENC = get_secret("COGNITO_AUDIENCE")


#MySQL 연동
DATABASES = {
    'default' : {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'mydb',
        'USER' : 'root',
        'PASSWORD' : '',
        'HOST' : '172.19.0.3',
        'PORT' : '3306',
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'mydb',  # 데이터베이스 이름
    #     'USER': 'root',  # 접속 사용자 이름
    #     'PASSWORD': '',  # 접속 비밀번호
    #     'HOST': 'localhost',
    #     'PORT': '13306',  # 기본 포트
    # }
}


#startapp으로 애플리케이션 생성할 경우 추가
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'signin',
    'signup',
    'itemlist',
    'rest_framework'
]


#Django-JWT 사용울 위한 설정
JWT_AUTH = { 
    'JWT_SECRET_KEY': SECRET_KEY, 
    'JWT_ALGORITHM': 'HS256', 
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=10), 
    'JWT_ALLOW_REFRESH': True, 
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(seconds=10), 
}


MIDDLEWARE = [
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ( 
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'django_cognito_jwt.JSONWebTokenAuthentication',
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}
ROOT_URLCONF = 'potato.urls'


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
            ],
        },
    },
]

WSGI_APPLICATION = 'potato.wsgi.application'


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


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#html이 css,img,vendor에 접근하는 경로
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] #static파일과 이미지파일은 static폴더에 저장
