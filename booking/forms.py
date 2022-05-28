from .models import Ticket
from django import forms

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['concert','user','order']
        widgets = {
            'concert': forms.Select(attrs={'class': 'form-control-sm'}),
            'user': forms.Select(attrs={'class': 'form-control-sm'}),
           
            'order': forms.NumberInput(attrs={'class': 'form-control-sm'}),
            }
       