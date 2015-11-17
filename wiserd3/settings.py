"""
Django settings for wiserd3 project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from celery import Celery

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ltn)r4*te4&f--z694+7m#fy9$-n)pe=&804xgk4g10wgn7uqa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'dataportal1-wiserd.cf.ac.uk']

# Application definition

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'jsonify',
    'widget_tweaks',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'dataportal3',
    'old',
    'old_qual',
    'django_hstore',

)

DJANGO_HSTORE_GLOBAL_REGISTER = False

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

AUTHENTICATION_BACKENDS = (
    # Default backend -- used to login by username in Django admin
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

ROOT_URLCONF = 'wiserd3.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates', 'templates/bootstrap_base'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',

                # "allauth.account.context_processors.account",
                # "allauth.socialaccount.context_processors.socialaccount",
            ],
        },
    },
]

TEMPLATE_CONTEXT_PROCESSORS = (
    # 'django.contrib.auth.context_processors.auth',
    # 'django.core.context_processors.debug',
    # 'django.core.context_processors.i18n',
    # 'django.core.context_processors.media',
    # 'django.core.context_processors.static',
    # 'django.core.context_processors.request',
    # 'django.contrib.messages.context_processors.messages',

    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

LOGIN_REDIRECT_URL = "/"

WSGI_APPLICATION = 'wiserd3.wsgi.application'

SITE_ID=1

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASE_ROUTERS = [
    'dataportal3.dbrouter.DBRouter',
    'old.old_dbrouter.OldDBRouter',
    'old_qual.qual_router.QualRouter'
]

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = './dataportal3/static/'

# TEMPLATE_DIRS = (
#     os.path.join(BASE_DIR,  'templates'),
#     os.path.join(BASE_DIR,  'templates/bootstrap_base'),
#
# )

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# from django.conf import global_settings
# import django.core.files.uploadhandler
# FILE_UPLOAD_HANDLERS = ('uploadprogresscachedhandler.UploadProgressCachedHandler', ) \
#     + global_settings.FILE_UPLOAD_HANDLERS


BROKER_URL = 'redis://localhost:6379/0'
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}  # 1 hour.
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
app = Celery('dataportal3.utils.ShapeFileImport', backend=BROKER_URL, broker=BROKER_URL)

nomis_uid = ''

TMP_DIR = '/home/ubuntu/'

TOPOJSON_DIR = '/home/ubuntu/DataPortalGeographies/'
TOPOJSON_OPTIONS = [
    {
        'name': 'Postcode District',
        'geog_short_code': 'pcode_d',
        'region_id': '2092957700TYPE274',
        'topojson_file': os.path.join(TOPOJSON_DIR, '05Wales_pcd_2012/output-fixed-1.json'),
        'topojson_file_high': os.path.join(TOPOJSON_DIR, '05Wales_pcd_2012/output-fixed-1.json')
    },
    {
        'name': 'Postcode Area',
        'geog_short_code': 'pcode_a',
        'region_id': '2092957700TYPE275',
        'topojson_file': os.path.join(TOPOJSON_DIR, '04Wales_pca_2012/output-fixed-1.json'),
        'topojson_file_high': os.path.join(TOPOJSON_DIR, '04Wales_pca_2012/output-fixed-1.json')
    },
    {
        'name': 'Postcode Sector',
        'geog_short_code': 'pcode',
        'region_id': '2092957700TYPE276',
        'topojson_file': os.path.join(TOPOJSON_DIR, '06Wales_pcs_2012/output-fixed-1.json'),
        'topojson_file_high': os.path.join(TOPOJSON_DIR, '06Wales_pcs_2012/output-fixed.json')
    },
    {
        'name': 'LSOA',
        'geog_short_code': 'lsoa',
        'region_id': '2092957700TYPE298',
        'topojson_file': os.path.join(TOPOJSON_DIR, '11Wales_lsoa_2011/output-fixed-1-k.json'),
        'topojson_file_high': os.path.join(TOPOJSON_DIR, '11Wales_lsoa_2011/output-fixed-1-k.json')
    },
    {
        'name': 'Unitary Authority',
        'geog_short_code': 'ua',
        'region_id': '2092957700TYPE464',
        'topojson_file': os.path.join(TOPOJSON_DIR, '14Wales_lad_unitaryauthority_2011/output-fixed-1.json'),
        'topojson_file_high': os.path.join(TOPOJSON_DIR, '14Wales_lad_unitaryauthority_2011/output-fixed-1.json')
    },
    {
        'name': 'Parliamentary Constituencies 2011',
        'geog_short_code': 'parl2011',
        'region_id': '2092957700TYPE460',
        'topojson_file': os.path.join(TOPOJSON_DIR, '13Wales_parlconstit_2011/output-fixed-1-4326.json'),
        'topojson_file_high': os.path.join(TOPOJSON_DIR, '13Wales_parlconstit_2011/output-fixed-1-4326.json')
    }
]

KNOWING_LOCALITIES_TABLES = [
    # {
    #     'display_name': 'Aberystwyth Locality Dissolved',
    #     'table_name': 'aberystwyth_locality_dissolved'
    # },
    # {
    #     'display_name': 'Bangor Locality Dissolved',
    #     'table_name': 'bangor_locality_dissolved'
    # },
    # {
    #     'display_name': 'Heads of_the Valleys',
    #     'table_name': 'heads_of_the_valleys'
    # }
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = ''
EMAIL_PORT = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

ACCOUNT_ADAPTER = 'dataportal3.account_logic.AccountAdapter'

# CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
MEDIA_ROOT = '/tmp/shapefiles/'
try:
    from wiserd3.settings_local import *
except ImportError:
    pass