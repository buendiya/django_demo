from django.conf.urls import patterns, url
from polls.views import * 


urlpatterns = patterns('',
                       url(r'^getname/$', get_name),
                       url(r'^thanks/$', thanks),
                       url(r'^get_latest_question/$', get_latest_question),
                       url(r'^create_question/$', create_question),
                       url(r'^get_question/$', get_question),
                       url(r'^login/$', login),
                       url(r'^session_test/$', sessioin_test),
                       url(r'^login_required_test/$', login_required_test),
                       )