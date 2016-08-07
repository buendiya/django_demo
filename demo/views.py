import logging

from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import render

logger = logging.getLogger('django.request')


def get_car(request):
    res = HttpResponse("Poll does not exist")
    res.set_cookie('hello', 'hello', 'world')
    logger.info('hello world')
    context = {'first_name': 'jing'}
#     return TemplateResponse(request, 'test_render.html', context)
    return render(request, 'test_render.html', context)
