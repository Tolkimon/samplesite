from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path, include

# Create your views here.

def index(request):
    return HttpResponse('hello world')

def help(request):
    return HttpResponse('This is help page')    