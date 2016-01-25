from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# each content_type model objects bound to an TaggedItem objects 
class TaggedItemGeneric(models.Model):
    tag = models.SlugField()
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):              # __unicode__ on Python 2
        return self.tag

# each content_type model class bound to an TaggedItem objects 
class TaggedItem(models.Model):
    tag = models.SlugField()
    content_type = models.ForeignKey(ContentType)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.tag