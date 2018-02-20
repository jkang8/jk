#!/usr/bin/env python
from __future__ import absolute_import, unicode_literals

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jk.settings.dev")
    if 'ENV' in os.environ:
        if os.environ['ENV'] == "dev":
            os.environ["DJANGO_SETTINGS_MODULE"] = "jk.settings.dev"
        elif os.environ['ENV'] == "production":
            os.environ["DJANGO_SETTINGS_MODULE"] = "jk.settings.production"

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
