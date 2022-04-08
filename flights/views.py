from django.http import HttpResponse
from .models import Flight  # Import Flight model
from airports.models import Airport  # Import airport model to get airport id and code
from .forms import FlightForm
from django.shortcuts import render

def index(request):
    # Fetch all flights
    form = FlightForm()
    return render(request, 'flights/index.html', {'form': form})

def flight_search(request, origin, destination):
    origin = Airport.objects.get(airport_code=origin)
    destination = Airport.objects.get(airport_code=destination)
    # Code to select flights from the database
    flights = Flight.objects.all()
    flight_list = ', '.join([f.origin.airport_code + "->" + f.destination.airport_code + " Airline Code: " +
                             f.airline.airline_code for f in flights])
    return HttpResponse('Showing flights: ' + flight_list)

def search(request):
    form = FlightForm(request.POST)
    if form.is_valid():
        flight = Flight.objects.get(id=1)
        return render(request, 'flights/flight_search.html', {'flight': flight})
