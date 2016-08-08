# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from snippets.models import Test


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    test = models.ForeignKey(Test, null=True, blank=True, related_name='choice')

    def __str__(self):
        return self.choice_text


class ProxyTest(Test):
    class Meta:
        proxy = True


class Author(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(null=True, blank=True)
    alias = models.CharField(max_length=50, null=True, blank=True)
    goes_by = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=300)
    num_awards = models.IntegerField()

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=300, verbose_name='名字')
    pages = models.IntegerField(verbose_name='页数')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='价格')
    rating = models.FloatField(verbose_name='排名')
    authors = models.ManyToManyField(Author, verbose_name='作者')
    publisher = models.ForeignKey(Publisher, verbose_name='出版社')
    pubdate = models.DateField(verbose_name='出版时间')

    def __str__(self):
        return self.name


class Chapter(models.Model):
    name = models.CharField(max_length=300)
    book = models.ForeignKey(Book, related_name='chapters')

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    registered_users = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Car(models.Model):
    name = models.CharField(max_length=255, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    photo = models.ImageField(upload_to='cars', blank=True)


# class RevealAccess(object):
#     """A data descriptor that sets and returns values
#        normally and prints a message logging their access.
#     """
# 
#     def __init__(self, initval=None, name='var'):
#         self.val = initval
#         self.name = name
# 
#     def __get__(self, obj, objtype):
#         print('Retrieving', self.name)
#         return self.val
# 
#     def __set__(self, obj, val):
#         print('Updating', self.name)
#         self.val = val
# 
# class CustomOneToOneField(models.OneToOneField):
#     serialize = RevealAccess(True, 'serialize')
# 
# 
# class Garage(models.Model):
#     car = CustomOneToOneField(Car, primary_key=True)

