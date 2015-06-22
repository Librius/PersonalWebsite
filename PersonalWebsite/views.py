__author__ = 'bonnie'

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the first page. And you can go to <a href='/blog'> BLOG </a>")