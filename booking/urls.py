from django.urls import path
from . import views




urlpatterns = [
    path("", views.ConcertList.as_view(), name="home"),
    path('booking/', views.test, name='booking'),
    path('book_ticket/(?P<concert_name>)/(?P<user_name>)/', views.book_ticket, name='book_ticket'),
]