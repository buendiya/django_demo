import json

from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.http import condition
from django.views.decorators.cache import cache_page
from django.db.transaction import non_atomic_requests
from django.views.decorators.vary import vary_on_headers
from django.contrib.auth.decorators import login_required

# Create your views here.
from polls.forms import NameForm, QuestionForm
from .models import Question

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('/polls/thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm(initial={'your_name': 'Hi there!'})

    return render(request, 'name.html', {'form': form})


def thanks(request):
    return render(request, 'thanks.html')


def latest_question(request):
    return Question.objects.all().latest("pub_date").pub_date


@condition(last_modified_func=latest_question)
def get_latest_question(request):
    form = QuestionForm(instance=Question.objects.all().latest("pub_date"))
    return render(request, 'question.html', {'form': form})


# @non_atomic_requests
def create_question(request):
    question = Question.objects.get_or_create(question_text='hello')[0]
    form = QuestionForm(instance=question)
    return render(request, 'question.html', {'form': form})

@cache_page(60 * 15)
@vary_on_headers('Accept-Encoding')
def get_question(request):
    print request.user
    form = QuestionForm(instance=Question.objects.all().last())
    return render(request, 'question.html', {'form': form})


def login(request):
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            return HttpResponse("You're logged in.")
        else:
            return HttpResponse("Please enable cookies and try again.")
    request.session.set_test_cookie()
    return render_to_response('login.html')


def sessioin_test(request):
    print request.session.items()
    request.session['hello'] = {'a':1}
#     request.session['hello']['a'] = 2
    print request.session.modified
    return HttpResponse('hello, world')


@login_required(redirect_field_name='my_redirect_field')
def login_required_test(request):
    return HttpResponse('login required')



