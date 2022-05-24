from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Concert
from .models import Ticket
from django.contrib.auth.models import User
from django.http import HttpResponse

class ConcertList(generic.ListView):
    model = Concert
    queryset = Concert.objects.all()
    template_name = "index.html"


def test(request):
    queryset = Concert.objects.all()
    items = Ticket.objects.all()
    
    context = {
        'items': items,
        'concert': queryset
    }
    return render(request, 'booking.html', context)

    
def book_ticket(request, concert_name, user_name, order):
    concert = get_object_or_404(Concert, name=concert_name)
    user = get_object_or_404(User, username=user_name)
    order = get_object_or_404(Ticket, order=order)
    ticket = Ticket()
    ticket.concert = concert
    ticket.user = user
    ticket.order = order
    ticket.save()

    return HttpResponse(" <h1>Ticket Booked!</h1>")
        

       

   




    
