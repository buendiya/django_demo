#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    sys.path.append('/Users/buendiya/Workspace/python/django-rest-framework')

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
