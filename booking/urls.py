from django.urls import path
from . import views




urlpatterns = [
    path("", views.ConcertList.as_view(), name="home"),
    path('booking', views.booking, name='booking'),
    path('book_ticket', views.book_ticket, name='book_ticket'),
    path('show_booking', views.show_booking, name='show_booking'),
    path('edit/<item_id>', views.edit_booking, name='edit'),
    
    
  
]