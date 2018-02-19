from __future__ import absolute_import, unicode_literals

from .base import *
import django_heroku

django_heroku.settings(locals())
DEBUG = False

try:
    from .local import *
except ImportError:
    pass
