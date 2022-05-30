from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Concert
from .models import Ticket
from .models import Venue
from .forms import TicketForm


class ConcertList(generic.ListView):
    '''
    A class based biew that renders
    Landing page.
    '''
    model = Concert
    queryset = Concert.objects.all()
    template_name = "index.html"


def show_booking(request):
    '''
    This function view, render the
    show_booking.html, where the user can see
    the booked tickets.
    '''
    items = Ticket.objects.all()
    context = {
        'items': items
        }
    return render(request, 'show_booking.html', context)


def about_booking(request):
    '''
    This function view, render the
    about_booking.html.
    '''
    things = Venue.objects.all()
    context = {
        'things': things

    }
    return render(request, 'about_booking.html', context)


def booking(request):
    '''
    This function view, render the
    booking.html and the user can
    see the booking form.
    '''
    items = Concert.objects.all()
    form = TicketForm()
    context = {
        'form': form,
        'items': items
    }
    return render(request, 'booking.html', context)


def edit_booking(request, item_id):
    '''
    This function will edit the booked tickets.
    The form will be populated from instance
    edit button/Ticket id. The user can edit and post,
    but the function lack the ability to add or
    decrease the total amount of tickets for
    the admin page.
    '''
    thing = get_object_or_404(Ticket, id=item_id)
    if request.method == 'POST':
        # check if the ticket order is 0
        if request.POST['order'] == '0':
            messages.error(request, (
                'Error! You can`t book 0 tickets.Please try again'))
            return redirect('booking')
        # check if the form is valid.
        form = TicketForm(request.POST, instance=thing)
        if form.is_valid():
            messages.success(request, (
                'You successfully updated your tickets!'))
            form.save()
            return redirect('show_booking')
    form = TicketForm(instance=thing)
    context = {
        'form': form
     }
    return render(request, 'edit_booking.html', context)


def book_ticket(request):
    '''
    This function will book tickets.
    It will also decrease the total
    amount of tickets when a user book
    tickets.
    '''
    concerts = Concert.objects.all()

    request_concert_id = int(request.POST['concert'])
    current_concert = None

    for concert in concerts:
        if concert.id == request_concert_id:
            current_concert = concert

    # Only validate if it is a post request
    if request.method == 'POST':
        # Check for min order of 0
        if request.POST['order'] == '0':
            messages.error(request, (
                'Error! You can`t book 0 tickets.Please try again'))
            return redirect('booking')

        # check  if the order is less than total tickets
        if int(request.POST['order']) >= current_concert.total_left:
            messages.error(request, (
                'You can not book more than the total amount of tickets!'))
            return redirect('booking')

        # Save form and update total tickets in Concert model (database)
        form = TicketForm(request.POST)
        if form.is_valid():
            current_concert.total_left -= int(request.POST['order'])
            current_concert.save()
        # Credit:Got this idea from:
        #  https://stackoverflow.com/questions/37773803/saving-modelform-with-user-id
            concert_goer = form.save(commit=False)
            concert_goer.user = request.user
            concert_goer.save()
        # end credit
            messages.success(request, (
                'You successfully booked your ticket or tickets!'))
            return redirect('show_booking')
    form.save()
    form = TicketForm()
    context = {
        'form': form
    }
    return render(request, 'booking.html', context)


def delete_booking(request, item_id):
    '''
    This function will let the user
    delete all the booked tickets.
    '''
    info = get_object_or_404(Ticket, id=item_id)
    messages.success(request, (
        'You successfully deleted your ticket or tickets!'))
    info.delete()
    return redirect('show_booking')
