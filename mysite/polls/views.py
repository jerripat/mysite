from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html = "Welcome to the Polls app, this is your home page."
    return HttpResponse(html)
