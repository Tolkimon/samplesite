from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path, include
from .models import Question
from .forms import QuestionModelsForm

# Create your views here.

def index(request):
    context = {}
    questions = Question.objects.all()
    context['questions'] = questions
    return render(request, 'index.html', context)


def help(request):
    return HttpResponse('This is help page')    


def detail(request, question_id):
    context = {}
    context['question'] = Question.objects.get(id = question_id)
    return render(request, 'details.html', context)


def update(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {}
    if request.method == 'POST':
        form = QuestionModelsForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return HttpResponse('Question updated')
        else:
            context['form'] = form
            render(request, 'update.html', context)
    else:
        context['form'] = QuestionModelsForm(instance=question)
        return render(request, 'update.html', context)