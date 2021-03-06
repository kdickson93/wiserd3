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
import pprint
from ast import literal_eval
from celery import Celery
# from dataportal3 import models

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
    'grappelli',
    'grappelli.dashboard',
    'grappelli_filters',
    'grappelli_menu',
    'grappelli_extensions',
    'explorer',
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
    'django_extensions',
    'rest_framework',
    'rest_framework_swagger',
    'django_filters'
)

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 99999,
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}

DJANGO_HSTORE_GLOBAL_REGISTER = False

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
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

LANGUAGE_CODE = 'en-US'

TIME_ZONE = 'UTC'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)
print LOCALE_PATHS

USE_I18N = True

USE_L10N = True

USE_TZ = False

from django.utils.translation import ugettext_lazy as _
LANGUAGES = (
    ('en', _('English')),
    ('cy', _('Welsh')),
)



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

NAW_LAYER_UUIDS = []

NAW_SEARCH_LAYER_UUIDS = []

WMS_LAYERS = [
    {
        'name': 'Inspire Wales',
        'url': 'http://inspire.wales.gov.uk/maps/wms?request=getCapabilities&version=1.3.0',
        'url_wms': 'http://inspire.wales.gov.uk/maps/wms',
        'filename': 'inspire_wales_wms.xml'
    },
    {
        'name': 'LLE Inspire NRW Wales',
        'url': 'http://lle.gov.wales/services/inspire-nrw/wms?request=getCapabilities',
        'url_wms': 'http://lle.gov.wales/services/inspire-nrw/wms',
        'filename': 'lle_inspire_nrw_wales_wms.xml'
    },
    {
        'name': 'LLE Inspire WG Wales',
        'url': 'http://lle.wales.gov.uk/services/inspire-wg/wms?request=getCapabilities',
        'url_wms': 'http://lle.wales.gov.uk/services/inspire-wg/wms',
        'filename': 'lle_inspire_wg_wales_wms.xml'
    },
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
ADMIN_EMAIL_ADDRESSES = ('',)

# This class governs login, signup etc
ACCOUNT_ADAPTER = 'dataportal3.account_logic.AccountAdapter'

ACCOUNT_USER_MODEL_EMAIL_FIELD= 'email'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_AUTHENTICATION_METHOD = 'email'

# CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
MEDIA_ROOT = '/tmp/shapefiles/'
try:
    from wiserd3.settings_local import *
except ImportError:
    pass

# Here be dragons.
# Hard coded dodgy translations of words
# based on the occurrence in a filename.
try:
    uid_path = os.path.join(BASE_DIR, './uids')
    if os.path.exists(uid_path):
        for uid_file in os.listdir(uid_path):
            if uid_file.endswith('.py') and not uid_file.startswith('list_'):

                # print os.path.abspath(uid_file)
                with open(os.path.join(uid_path, uid_file)) as var_file:
                    var = var_file.read()
                    var_read = literal_eval(var)
                    # print var_read

                    ordered_items = {}
                    unordered = []
                    for item in var_read:
                        if 'count' in item:
                            # print item['count']
                            ordered_items[item['count']] = item
                        else:
                            unordered.append(item)

                    sorted_items = [ordered_items[k] for k in sorted(ordered_items)]
                    sorted_items.extend(unordered)

                    en_name = uid_file.replace('.py', '')
                    cy_name = en_name

                    if 'regions' in en_name.lower():
                        cy_name = 'Rhanbarth'

                    if 'constituencies' in en_name.lower():
                        cy_name = 'Etholaeth'

                    values = {
                        'description': en_name,
                        'description_cy': cy_name,
                        'item_list': sorted_items
                    }
                    # print pprint.pformat(values)

                    NAW_SEARCH_LAYER_UUIDS.append(values)
except Exception as e:
    print e