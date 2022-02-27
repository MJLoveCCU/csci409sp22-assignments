# Load path from django.urls
from django.urls import path
# load this applications views.py file
from . import views

# Define url patterns
urlpatterns = [
    # Get index view
    # example url: /airports/
    path('/', views.index),
    # Show airport info
    # Example url /airports/MYR
    # NOTICE: the airport_code parameter in the url matches
    #   the parameter in the airport_info function
    path('/<int:confirmation_number>', views.ticket_search),
]
