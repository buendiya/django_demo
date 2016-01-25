import datetime
from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericRelation

from contenttype_generic.models import TaggedItemGeneric

QUESTION_STATUS_LIST = [[0, u'have answer'],
                     [1, u'no answer'],
                     ]

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now=True)
    status = models.PositiveIntegerField(choices=QUESTION_STATUS_LIST, null=True, blank=True, default=1)
    tags = GenericRelation(TaggedItemGeneric)
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text