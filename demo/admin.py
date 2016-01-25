from django.contrib import admin
from .models import Choice, Author, Publisher, Book, Store, Chapter

 
admin.site.register(Choice)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Store)
admin.site.register(Chapter)