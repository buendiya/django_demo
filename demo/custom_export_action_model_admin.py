# -*- coding: utf-8 -*-

from import_export.admin import ImportExportActionModelAdmin
from import_export.resources import ModelResource, ModelDeclarativeMetaclass
from import_export import fields

from .models import Book


class CustomModelResourceMetaClass(ModelDeclarativeMetaclass):
    """
    resourece_fields: only support model fields and class method 
    """
    def __new__(cls, name, bases, attrs):
        model_admin = attrs['model_admin']
        resource_fields = model_admin.resource_fields 
        model = model_admin.model
        all_model_field_names = model._meta.get_all_field_names()
        resourece_fields_final = []
        export_order = []
        for resource_field in resource_fields:
            if resource_field in all_model_field_names:
                field = model._meta.get_field(resource_field)
                attrs[resource_field] = fields.Field(attribute=resource_field, column_name=field.verbose_name)
                resourece_fields_final.append(resource_field)
                export_order.append(resource_field)
            else:
                attr = getattr(model_admin, resource_field)
                attrs[resource_field] = fields.Field(column_name=getattr(attr, 'short_description', resource_field))
                attrs['dehydrate_%s' % resource_field] = attr
                export_order.append(resource_field)

        attrs['Meta'] = type('Meta', (), {'model': model, 'fields': resourece_fields_final, 'export_order': export_order})

        return super(CustomModelResourceMetaClass, cls).__new__(cls, name, bases, attrs)



class BookModelResource(ModelResource):
    name = fields.Field(column_name=u'名字', attribute='name')
    upper_case_name = fields.Field(column_name=u'大写名字', attribute='name')

    class Meta:
        model = Book
        fields = ('pages', 'publisher', 'name', 'upper_case_name', )
        export_order = ('name', 'upper_case_name', 'publisher', )

    def dehydrate_upper_case_name(self, obj):
        return obj.name.upper()


class CustomeExportActionModelAdmin(ImportExportActionModelAdmin):

    def get_export_resource_class(self):
        return CustomModelResourceMetaClass('temp_resource_class', (ModelResource, ), {'model_admin': self})
        # return BookModelResource
