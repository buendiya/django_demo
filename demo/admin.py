# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Choice, Author, Publisher, Book, Store, Chapter, Car, ProxyTest
from nested_inline.admin import NestedModelAdmin, NestedTabularInline

from .custom_export_action_model_admin import CustomeExportActionModelAdmin


class BookAdmin(CustomeExportActionModelAdmin):
    model = Book
    list_display = ('name', 'pages', 'publisher', 'upper_case_name', )
    resource_fields = ('name', 'pages', 'publisher', 'upper_case_name', )

    def upper_case_name(self, obj):
        return obj.name.upper()
    upper_case_name.short_description = '大写名字'


class ChapterNestedInlineAdmin(admin.TabularInline):
    model = Chapter
    extra = 0


class AuthorlineAdmin(admin.TabularInline):
    model = Author
    extra = 0


class BookInlineAdmin(admin.TabularInline):
    model = Book
    extra = 0


class PublisherAdmin(admin.ModelAdmin):
    model = Publisher
    extra = 0


#     def save_formset(self, request, form, formset, change):
#         if formset.model is Book:
#             for form in formset:
#                 form.instance.pages = form.instance.pages - 1
#         super(PublisherNestedAdmin, self).save_formset(request, form, formset, change)
# 
#     def get_inline_formsets(self, request, formsets, inline_instances,
#                             obj=None):
#         inline_admin_formsets = super(PublisherNestedAdmin, self).get_inline_formsets(request, formsets, inline_instances, obj)
#         for inline_admin_formset in inline_admin_formsets:
#             if inline_admin_formset.formset.model is Book:
#                 for form in inline_admin_formset.formset:
#                     form.initial['pages'] = form.initial['pages'] + 1
#         return inline_admin_formsets


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
