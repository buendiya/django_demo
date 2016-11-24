# -*- coding: utf-8 -*-
"""
为了验证：Django provides full support for anonymous sessions.

输出如下：
set_session request count: 1
session is empty
[09/Oct/2016 16:14:53]"GET /session_demo/set_session/ HTTP/1.1" 200 12
set_session request count: 2
session value:  hello, world
[09/Oct/2016 16:15:00]"GET /session_demo/set_session/ HTTP/1.1" 200 12

所有请求都是anonymous, 第一个请求进来时，session为空；第一个请求完成之后，可以在client端的browser的cookie里看到session_id
第二个请求进来时，会带上session_id，在SessionMiddleware会给request附上正确的session
"""
from django.http import HttpResponse


SET_SESSION_REQUEST_COUNT = 0


def set_session(request):
    global SET_SESSION_REQUEST_COUNT
    SET_SESSION_REQUEST_COUNT += 1
    print 'set_session request count: %s' % SET_SESSION_REQUEST_COUNT

    if request.session.is_empty():
        print 'session is empty'
        request.session['test'] = 'hello, world'
    else:
        print 'session value: ', request.session['test']
    return HttpResponse('hello, world')
