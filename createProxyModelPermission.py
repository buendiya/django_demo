from __future__ import unicode_literals, absolute_import, division
import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()

from django.contrib.auth.management import _get_all_permissions
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.apps import apps
from django.utils.encoding import smart_unicode

from demo.models import ProxyTest


def check_content_type():
    for model in apps.get_models():
        opts = model._meta
        if ContentType.objects.filter(app_label=opts.app_label, model=opts.object_name.lower()).exists():
            if model is ProxyTest:
                ctype = ContentType.objects.get(app_label=opts.app_label, model=opts.object_name.lower())
                for codename, name in _get_all_permissions(opts, ctype):
                    print codename, name


def createProxyPermission():
    for model in apps.get_models():
        opts = model._meta
        ctype, created = ContentType.objects.get_or_create(
            app_label=opts.app_label,
            model=opts.object_name.lower(),
            defaults={'name': smart_unicode(opts.verbose_name_raw)})
        if created:
            print 'Create ContentType: %s' % ctype

        for codename, name in _get_all_permissions(opts, ctype):
            p, created = Permission.objects.get_or_create(
                codename=codename,
                content_type=ctype,
                defaults={'name': name})
            if created:
                sys.stdout.write('Adding permission {}\n'.format(p))

if __name__ == '__main__':
#     check_content_type()
    createProxyPermission()
