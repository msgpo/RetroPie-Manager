# -*- coding: utf-8 -*-
"""
Django settings for recalbox-manager project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
#from manager_frontend.utils.manifest import RecalboxManifestParser

gettext = lambda s: s

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.join(BASE_DIR, 'project')

SITE_ID = 1
# If not empty, use this instead of Site framework to know the name and use 
# a trick to find the host ip
SITE_FIXED = {
    'name': "Retropie Manager",
    'ip': None, # If None find the ip automatically, else use a string to define another hostname
    'port': '8001', # If None no port is appended to hostname, so the server have to be reachable from port 80
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(_0!&^^xekahfp=s5(9+^wlq6gvn6z90%i*p+wn^4ir+mvl4lx'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    #'django.contrib.sites',
    'django.contrib.staticfiles',
    
    'autobreadcrumbs',
    
    'project.assets_cartographer',
    'project.recalbox_manifest',
    'project.manager_frontend',
    
    #'ajaxuploader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'project.utils.context_processors.site_metas',
                'project.utils.context_processors.manager_version',
                'autobreadcrumbs.context_processors.AutoBreadcrumbsContext',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en', gettext('English')),
    ('fr', gettext('French')),
    ('de', gettext('German')),
)

TIME_ZONE = None

USE_I18N = True

USE_L10N = True

USE_TZ = False

LOCALE_PATHS = (
    os.path.join(PROJECT_DIR, 'locale'),
)

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, "webapp_statics"),
)

# For Django messages framework to avoid database requests
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

# For assets management
ASSETS_PACKAGED = not(DEBUG)
ASSETS_STRICT = False
ASSETS_MAP_FILEPATH = os.path.join(PROJECT_DIR, "assets.json")
ASSETS_TAG_TEMPLATES = {
    "javascripts": "assets/javascript_tag.html",
    "stylesheets": "assets/stylesheet_tag.html",
}

#
# Recalbox needed paths
#

# Path to directory that contains bios file
RECALBOX_BIOS_PATH = "/home/pi/RetroPie/BIOS"
# Path to directory that contains system roms directories
RECALBOX_ROMS_PATH = '/home/pi/RetroPie/roms'
# Path to directory that contains system saves
#RECALBOX_SAVES_PATH = '/home/pi/RetroPie/roms'
# Path to the Retroarch configuration file
RECALBOX_CONF_PATH = '/opt/retropie/configs/all/retroarch.cfg'
# Path to the Retroarch configuration backup file
RECALBOX_CONF_BACKUP_PATH = '/opt/retropie/configs/all/retroarch.cfg.bak'
# Path to the ES configuration file
ES_CONF_PATH = '/etc/emulationstation/es_systems.cfg'
# Path to the ES configuration backup file
ES_CONF_BACKUP_PATH = '/etc/emulationstation/es_systems.cfg.bak'
# Path to autostart.sh
AS_SCRIPT_PATH = '/opt/retropie/configs/all/autostart.sh'
# Path autostart.sh backup file
AS_SCRIPT_BACKUP_PATH = '/opt/retropie/configs/all/autostart.sh.bak'
# Path to the Recalbox logs file
RECALBOX_LOGFILE_PATH = "/opt/retropie/configs/all/emulationstation/es_log.txt"
# Path to the Recalbox manifest file (actually shipped into manager project)
RECALBOX_MANIFEST_FILEPATH = os.path.join(PROJECT_DIR, 'MANIFEST.xml')

# Default empty entry for unknowed system from Manifest
RECALBOX_SYSTEM_DEFAULT = {
    'name': 'Unknow',
    'extensions': [],
    'bios': [],
}

# Blocking time during psutil watch for cpu charge in second (float number)
RECALBOX_PSUTIL_CPU_INTERVAL = 0.5 # 0.1 seems a little too low but 1.0 add 1s on page loading time
