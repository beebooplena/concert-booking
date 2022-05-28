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



def show_booking(request):
    items = Ticket.objects.all()
    context = {
        'items':items

    }
    return render(request, 'show_booking.html', context)

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


def edit_booking(request, item_id):
    thing = get_object_or_404(Ticket, id=item_id)
    if request.method == 'POST':
        if request.POST['order'] == '0':

            messages.error(request, ('Error! You can`t book 0 tickets.Please try again'))
            return redirect('booking')
        form = TicketForm(request.POST, instance=thing)
        if form.is_valid():
            messages.success(request, ('You successfully updated your tickets!'))
            
            form.save()
            return redirect('show_booking')
    form = TicketForm(instance=thing)
    context = {
        'form': form
    }
    return render(request, 'edit_booking.html', context)








 

    
def book_ticket(request):
    if request.method == 'POST':
        if request.POST['order'] == '0':

            messages.error(request, ('Error! You can`t book 0 tickets.Please try again'))
            return redirect('booking')
            
        form = TicketForm(request.POST)
        if form.is_valid():
            messages.success(request, ('You successfully booked your ticket or tickets!'))
            
            form.save()
            return redirect('show_booking')
            
    else:
        messages.error(request, ('Error! Something went wrong. Please try again.'))
        return redirect('booking')

        
    form = TicketForm()
    context = {
        'form': form
    }
    return render(request, 'booking.html', context)
   
def delete_booking(request, item_id):
    info = get_object_or_404(Ticket, id=item_id)
    messages.success(request, ('You successfully deleted your ticket or tickets!'))
    info.delete()
    return redirect('home')