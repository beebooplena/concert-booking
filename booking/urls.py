from django.urls import path
from . import views




urlpatterns = [
    path("", views.ConcertList.as_view(), name="home"),
    path('booking/', views.book, name='booking'),
    path('book_ticket/', views.book_ticket, name='book_ticket'),
    path('show', views.show, name='show'),
]