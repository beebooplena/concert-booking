from django.contrib import admin
from .models import Venue
from .models import Concert
from .models import Ticket

admin.site.register(Venue)
admin.site.register(Concert)
admin.site.register(Ticket)
