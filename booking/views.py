from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from .models import Concert
from .models import Ticket
from .models import Venue
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


def about_booking(request):
    things = Venue.objects.all()
    context = {
        'things':things

    }
    return render(request, 'about_booking.html', context)

def booking(request):
    items = Concert.objects.all()
    

   

        
    form = TicketForm()
    context = {
        'form': form,
        'items': items
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
    concents = Concert.objects.all()

    request_concent_Id = int(request.POST['concert'])
    current_concent = None

    for concent in concents:
        if concent.id == request_concent_Id:
            current_concent = concent

    # Only validate if it is post request
    if request.method == 'POST':
        # Check for min order of 0
        if request.POST['order'] == '0':
            messages.error(request, ('Error! You can`t book 0 tickets.Please try again'))
            return redirect('booking')

        # check  if order is les then tickes number
        if int(request.POST['order']) >= current_concent.total_left:
            messages.error(request, ('You can not shoo...'))
            return redirect('booking')

        # Save ticket form to database
        form = TicketForm(request.POST)
        if form.is_valid():
        
            current_concent.total_left-=int(request.POST['order'])
            current_concent.save()
            thought = form.save(commit=False)
            
            # Save change ticket number in Concent table (database)
          
            
            

            thought.user = request.user
            thought.save()
            messages.success(request, ('You successfully booked your ticket or tickets!'))
            return redirect('show_booking')

    form.save()
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
    