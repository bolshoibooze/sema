from __future__ import absolute_import

import logging
import os.path
import datetime
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

logger = logging.getLogger()

ADMINS = (
     ('Arthur Mwai', 'mwaigaryan@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test_db',                  
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                    
        'PORT': '',                     
    }
}


ALLOWED_HOSTS = ['*']


TIME_ZONE = 'Africa/Nairobi'


LANGUAGE_CODE = 'en-us'

SITE_ID = 1


USE_I18N = True


USE_L10N = True


USE_TZ = True


MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'static/media/')
#MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media/')

MEDIA_URL = '/static/media/'

STATIC_ROOT = ''

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), 'static'),
   
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


SECRET_KEY = 'ystmh_s#%xi+!of^^xogokl_76via2l(k+_xq-4)+(rcx$+%18'


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',    
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    #'django.core.context_processors.csrf',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'yawdadmin.middleware.PopupMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    
)

ROOT_URLCONF = 'digicheq.urls'

HTML_MINIFY = True

CSRF_COOKIE_DOMAIN = None

WSGI_APPLICATION = 'digicheq.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'yawdadmin',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.markup',
    'django.contrib.sitemaps',
    #'django.contrib.formtools',
    
    #local apps
    'accounts',
    'chequebook',
    'ua_detector',
    'notifications',
    'blockchain',
    'banks',
    
    #3rd party
    'admin_honeypot',
    'signal_hub',
    'djcelery',
    'tastypie',
    
    
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

AUTH_USER_MODEL = 'accounts.CustomUser'

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler' 

CELERYBEAT_SCHEDULE = {}



CURRENCY = (
   ('K sh','K sh'),
   ('USD','USD'),
   ('AUD','AUD'),
   ('Other','Other')
)

TIME = (
   ('Today','Today'),
   ('1-week','1-week'),
   ('2-weeks','2-weeks'),
   ('3-weeks','3-weeks'),
   ('1-month','1-month')
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

import djcelery
djcelery.setup_loader()
