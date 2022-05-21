from django.urls import path
from . import views


urlpatterns = [
    path("", views.ConcertList.as_view(), name="home"),
]