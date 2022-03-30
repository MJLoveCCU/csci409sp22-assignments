from django.http import HttpResponse
from django.shortcuts import render # import the render library to make loading templates easier
from .models import Airport

def index(request):
    # Fetch all airports from the database
    airports = Airport.objects.all()
    # Place all airports into a context variable for retrieval in the view.
    context = {'airports': airports}
    return render(request, 'airports/index.html', context)

def airport_info(request, airport_code):
    # Fetch the airport by a certain code
    # Remember as we are only expecting one airport per code we should use get
    runway = Airport.objects.get(airport_code=airport_code)
    context = {'runway': runway}
    # Display the airport name and code
    return render(request, 'airports/airport.html', context)


