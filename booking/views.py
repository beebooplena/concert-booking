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
    items = Concert.objects.all()
    
    context = {
        'items': items
        
    }
        

    return render(request, 'booking.html', context)

    
def book_ticket(request, concert_name, user_name):

    concert = get_object_or_404(Concert, name=concert_name)
    user = get_object_or_404(User, username=user_name)
    ticket = Ticket()
    ticket.concert = concert
    ticket.user = user
    ticket.save()

    return HttpResponse(" <h1>Ticket Booked!</h1>")
        

       

   




    
