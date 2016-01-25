from django.contrib import admin

# Register your models here.
from polls.models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date', 'status'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date', 'status', 'question_text']
    search_fields = ['question_text']
#     actions_on_bottom = True
#     date_hierarchy = 'pub_date'

admin.site.register(Question, QuestionAdmin)