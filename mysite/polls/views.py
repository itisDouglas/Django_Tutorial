from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question

# Create your views here.
#rule for views:
#a view needs to return an HttpResponse object or raise exception like Http 404

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #loading up the template
    template = loader.get_template('polls/index.html')
    #context is a dictionary mapping template variable names to Python objects
    context = {
        'latest_question_list': latest_question_list,
    }
    #render function takes request objects as first argument
    #template name as second argument
    #dictionary as optional third argument
    #returns an HttpResponse object of the given template 
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #get_object_or_404() takes django model as 1st argument
    #takes arbitrary number of keyword arguments as secon argument
    #passes these to the get() of the model's manager
    #raises http 404 if object doesn't exist
    question = get_object_or_404(Question,
    pk=question_id)
    return render(request, 'polls/detail.html',{'question':question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


