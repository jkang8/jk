from __future__ import absolute_import, unicode_literals

from .base import *
import django_heroku

django_heroku.settings(locals())

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False

ALLOWED_HOSTS = (
    'morning-sea-64598.herokuapp.com',
    'johnkang.co',
    'www.johnkang.co',
)


MIDDLEWARE_CLASSES = (
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

try:
    from .local import *
except ImportError:
    pass
