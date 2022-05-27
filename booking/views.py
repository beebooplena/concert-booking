from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Concert
from .models import Ticket
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import TicketForm




class ConcertList(generic.ListView):
    model = Concert
    queryset = Concert.objects.all()
    template_name = "index.html"


def booking(request):

    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('home')
    form = TicketForm()
    context = {
        'form': form
    }
    return render(request, 'booking.html', context)








 

    
def book_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('home')
    form = TicketForm()
    context = {
        'form': form
    }
    return render(request, 'booking.html', context)
   
             
 

# def book_ticket(request):
#     if request.method == "POST":
#         if request.POST['quanty'] == '0':
#             messages.error(request, ('Error! You can`t book 0 tickets.Please try again'))
#             return redirect('booking')
#         else:
            
#             quanty = request.POST['quanty']
#             concertId = request.POST['concert_name']
#             username = request.user.username
#             user = get_object_or_404(User, username=username)
            
#             concert = get_object_or_404(Concert, id=concertId)
#             ticket = Ticket()
#             ticket.concert = concert
#             ticket.user = user
#             ticket.order = quanty
#             ticket.save()
#             messages.success(request, ('You successfully booked your ticket or tickets!'))
#             return redirect('show')
# else:
#         messages.error(request, ('Error! Something went wrong. Please try again.'))
#         return redirect('booking')


    
        
        
    

        
        
        
        
    


        
    

        

       

   




    
