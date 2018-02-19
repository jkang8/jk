from __future__ import absolute_import, unicode_literals

from .base import *
import django_heroku

django_heroku.settings(locals())
DEBUG = False

ALLOWED_HOSTS = (
    'morning-sea-64598.herokuapp.com',
    'johnkang.co',
)

try:
    from .local import *
except ImportError:
    pass
