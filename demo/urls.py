from django.conf.urls import url

from .views import get_car
from . import views

# API endpoints
urlpatterns = [
    url(r'^get_car/$', get_car, name='demo_car'),
    url(r'^car/$', views.CarView.as_view()),
    url(r'^garage/(?P<pk>[0-9]+)/$', views.GarageView.as_view()),
]

