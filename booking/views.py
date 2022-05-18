from django.shortcuts import render
from django.views import generic
from .models import Venue
from .models import Concert


class ConcertList(generic.ListView):
    model = Concert
    queryset = Concert.objects.order_by('concert_created')
    template_name = 'index.html'
    paginate_by = 6
