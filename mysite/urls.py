from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

from .views import check_status


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include("polls.urls")),
    url(r'^snippets/', include("snippets.urls")),
    url(r'^_status$', check_status),
    url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True
        }),
    url(r'^demo/', include("demo.urls")),
    url(r'^session_demo/', include("session_demo.urls")),
]
