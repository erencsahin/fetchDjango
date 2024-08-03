from pathlib import Path
from mongoengine import connect
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-!e^tgh$z*lwjf*#kh$d$u!&e8c-b*i-8#*1!=068f3$gs4+()n'
DEBUG = True
ALLOWED_HOSTS = ['192.168.5.101', 'localhost','http://localhost:3000',
    'http://192.168.5.100','http://192.168.5.100:3000','https://127.0.0.1']

AZURE_ACCOUNT_NAME = 'myaccount'
AZURE_ACCOUNT_KEY = '00000000'
AZURE_CONTAINER_NAME = 'wext-ai-images'
AZURE_CONNECTION_STRING_DEV = 'DefaultEndpointsProtocol=https;AccountName=wextimagedb;AccountKey=QGAOPPtvDv+iLd6v2hiw7ph8EPRFAiLOSm5cNydc2bBHRSE+m7eDrtM2F2K1paVLFTxVXrTRtrW3+ASthbTczA==;EndpointSuffix=core.windows.net'
AZURE_CONNECTION_STRING_PROD = 'DefaultEndpointsProtocol=https;AccountName=wextimagedb;AccountKey=QGAOPPtvDv+iLd6v2hiw7ph8EPRFAiLOSm5cNydc2bBHRSE+m7eDrtM2F2K1paVLFTxVXrTRtrW3+ASthbTczA==;EndpointSuffix=core.windows.net'

INSTALLED_APPS = [
    'corsheaders',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'images',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS=[
    "http://localhost:3000",
    "http://192.168.5.103:3000"
]
CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'image_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

MY_API_KEY = "CAo1N5NFk2blrJeHBXb1s7PbJA6K2TWsROGjL3F8AJ2Eww9wG8BpveJi"
WSGI_APPLICATION = 'image_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

connect(
    db='mytextdb',
    host='localhost',
    port=27017
)

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
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'