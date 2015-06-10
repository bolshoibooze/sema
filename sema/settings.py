from __future__ import absolute_import

import logging
import os.path
import datetime
from datetime import timedelta

logger = logging.getLogger()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))




DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']




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
    
    #local apps
    'ua_detector',
    'therapists',
    'yawdadmin',
    'payments',
    'accounts',
    'chat',
    
    #3rd party
    'admin_honeypot',
    'djcelery',
    'tastypie',
)

AUTH_USER_MODEL = 'accounts.CustomUser'

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler' 

CELERYBEAT_SCHEDULE = {}

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)



TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',    
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

HTML_MINIFY = True

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

ROOT_URLCONF = 'sema.urls'

WSGI_APPLICATION = 'sema.wsgi.application'

SECRET_KEY = '@(8x3x0r&l65+r728k77^dva+*%d$a=nqwb45hq1!$rxo3=u!*'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
#TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media/')

MEDIA_URL = '/static/media/'

STATIC_ROOT = ''

STATIC_URL = '/static/'



import djcelery
djcelery.setup_loader()
