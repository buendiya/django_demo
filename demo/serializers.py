
from .models import Car, Book, Garage
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car


class GarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = ('car', )


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
