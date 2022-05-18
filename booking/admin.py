from django.contrib import admin
from .models import Venue
from .models import Concert

admin.site.register(Venue)
admin.site.register(Concert)
