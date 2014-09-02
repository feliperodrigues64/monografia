import os
from base import *
from decouple import ConfigIni
import dj_database_url


config = ConfigIni(PROJECT_DIR.child('infra_confs')+'/settings.ini')
# ######### INSTALLED APPS CONFIGURATION

INSTALLED_APPS += (
    'django_nose',
    'nose',
)

# ######### TEST SETTINGS
os.environ['REUSE_DB'] = "1"
SOUTH_TESTS_MIGRATE = False
TEST_RUNNER = "django_nose.NoseTestSuiteRunner"
TEST_DISCOVER_TOP_LEVEL = PROJECT_DIR
TEST_DISCOVER_ROOT = PROJECT_DIR
TEST_DISCOVER_PATTERN = "test_*"
NOSE_ARGS = [
    '--verbosity=2',
    '-x',
    '-d',
    '--with-specplugin',
    '--with-xtraceback',
    '--with-progressive',
]
# ######### END TEST SETTINGS

# ######### DEBUG CONFIGURATION
DEBUG = True

TEMPLATE_DEBUG = DEBUG

COMPRESS_ENABLED = not DEBUG
# ######### END DEBUG CONFIGURATION


# ######### DATABASE CONFIGURATION
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}
# ######### END DATABASE CONFIGURATION
