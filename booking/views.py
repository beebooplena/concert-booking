from django.shortcuts import render
from django.views import generic
from .models import Venue
from .models import Concert


class ConcertList(generic.ListView):
    model = Concert
    template_name = 'index.html'
    paginate_by = 6
