import logging

from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import render

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import mixins

from .models import Car, Garage
from .serializers import CarSerializer, GarageSerializer

logger = logging.getLogger('django.request')


@api_view()
def get_car(request):
    logger.info('hello world')
    res = {'first_name': 'jing'}
    return Response(res)


class CarView(mixins.RetrieveModelMixin,
              mixins.CreateModelMixin,
              generics.GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get(self, request, *args, **kwargs):
        self.kwargs.update({'pk': 1})
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GarageView(mixins.RetrieveModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = Garage.objects.all()
    serializer_class = GarageSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



