
from .models import Car, Book
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
