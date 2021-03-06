"""
Django settings for MArtPro project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 引入extapps和myapps的两个sources root目录
sys.path.insert(0, os.path.join(BASE_DIR, 'myapps'))
sys.path.insert(1, os.path.join(BASE_DIR, 'extapps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rhi67s4im$%5v%%oj=6z31l+qshpc&jcsi_+kgk1&)v+ib_p0$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'art',
    'user',
    'xadmin',
    'crispy_forms',
    'DjangoUeditor',
    'djcelery',  # 引入Django-Celery app
    'rest_framework'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MArtPro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'MArtPro.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'  # 网络访问静态资源的路径

# 配置静态文件存储的位置
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# 配置媒体文件的存储位置(上传的文件存放的ROOT目录)
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/uploads')

# 配置访问媒体文件的URL
MEDIA_URL = '/static/uploads/'


# ----REDIS Cache缓存-----
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1/3',  # 'redis://:password@127.0.0.1/3'
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
        }
    }
}

# ---end Cache---

# 配置Session
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # 使用缓存


# 配置REDIDS的连接
REDIS_CACHE = {
    'host': '127.0.0.1',
    'db': 3,
    'port': 6379
}


# -----配置 Django-Celery-----
import djcelery
from celery.schedules import crontab, timedelta

djcelery.setup_loader()  # 加载djcelery应用

# 配置消息中件间
BROKER_URL = 'redis://127.0.0.1:6379/5'
CELERY_IMPORTS = ('art.tasks',)  # 初始导入 celery任务位置
CELERY_TIMEZONE = 'Asia/Shanghai'  # 时区

# 配置任务定时队列存储的位置
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'


# 配置任务任务
CELERYBEAT_SCHEDULE = {
    u'定时发邮件': {
        'task': 'art.tasks.sendEmailLog',
        'schedule': timedelta(seconds=10),
        'args': ()
    }
}

# ----end Django-Celery------


# ---配置日志---
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters':{  # 日志格式器
        'simple': {
            'format': '[%(asctime)s]->%(module)s/%(funcName)s:%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {  # 日志处理器
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'logFile': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'simple',
            'filename': 'mart.log'
        }
    },
    'loggers': {  # 日志记录器
        'info': {
            'handlers': ('console', 'logFile'),
            'level': 'INFO',
            'propagate': False
        }
    }
}

# 设置Django_REST_Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':[
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

