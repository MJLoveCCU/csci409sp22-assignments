from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello from airports');

def airport_info(request, airport_code):
    return HttpResponse('Showing info for airport: ' + airport_code);


