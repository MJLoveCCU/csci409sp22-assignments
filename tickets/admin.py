from django.contrib import admin
from .models import Reservation, Ticket

# Register your models here.
class TicketInLine(admin.StackedInline):
    model = Ticket
    extra = 2

class ReservationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['flight', 'num_people', 'total_cost']})
    ]
    inlines = [TicketInLine]

admin.site.register(Reservation, ReservationAdmin)