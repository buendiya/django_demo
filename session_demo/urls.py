from django.conf.urls import url

from .views import set_session

# API endpoints
urlpatterns = [
    url(r'^set_session/$', set_session, name='set_session'),
]
