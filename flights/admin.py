from django.contrib import admin
from .models import Flight, Airline

# Register your models here.
class AirlineAdmin(admin.ModelAdmin):
    model = Airline

class FlightAdmin(admin.ModelAdmin):
    fieldsets = [  # THE FIELDS HAVE TO MATCH THE LAYOUT OF THE MODEL. NO CAPS.
        (None, {'fields': ['airline', 'flight_number']}),
        (None, {'fields': ['origin', 'destination']}),
        ('Departure and Arrival Time', {'fields': ['departure', 'arrival'], 'classes': ['collapse']})
    ]


admin.site.register(Airline, AirlineAdmin)
admin.site.register(Flight, FlightAdmin)
