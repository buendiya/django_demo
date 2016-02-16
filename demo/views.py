import logging

from django.http import HttpResponse
from django.template.response import TemplateResponse

logger = logging.getLogger('django.request')


def get_car(request):
    res = HttpResponse("Poll does not exist")
    res.set_cookie('hello', 'world')
    logger.info('hello world')
    return res
