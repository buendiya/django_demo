from django.conf.urls import url

from .views import get_car

# API endpoints
urlpatterns = [
    url(r'^car/$',
        get_car,
        name='user-detail')
]

