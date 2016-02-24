import logging

from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import render

logger = logging.getLogger('django.request')


def get_car(request):
    res = HttpResponse("Poll does not exist")
    res.set_cookie('hello', 'world')
    logger.info('hello world')
    context = {'first_name': 'jing'}
    # the following do the same thing
#     return TemplateResponse(request, 'test_render.html', context)
    return render(request, 'test_render.html', context)
