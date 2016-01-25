from django.db import models
from snippets.models import Test


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    test = models.ForeignKey(Test, null=True, blank=True, related_name='choice')

    def __str__(self):
        return self.choice_text


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
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    pubdate = models.DateField()
    
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

