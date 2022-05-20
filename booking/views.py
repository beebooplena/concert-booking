from django.shortcuts import render
from django.views import generic
from .models import Concert


class ConcertList(generic.ListView):
    model = Concert
    queryset = Concert.objects.all()
    template_name = "index.html"
    