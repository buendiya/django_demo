from django import forms
from .models import Question

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'