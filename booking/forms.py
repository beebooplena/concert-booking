'''
imported forms and Ticket model
'''
from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    '''
    This is the form for booking tickets.
    '''
    class Meta:
        '''
        The inner class from models.py
        '''
        model = Ticket
        fields = ['concert', 'user', 'order']
        exclude = ('user',)
        widgets = {
            'concert': forms.Select(attrs={'class': 'form-control-sm'}),
            'user': forms.Select(attrs={'class': 'form-control-sm'}),
            'order': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            }
