from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello from tickets');
def ticket_search(request, confirmation_number):
    return HttpResponse('Showing tickets for confirmation number: ' + str(confirmation_number));
