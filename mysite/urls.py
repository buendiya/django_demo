from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import check_status

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include("polls.urls")),
    url(r'^snippets/', include("snippets.urls")),
    url(r'^_status$', check_status),
)
