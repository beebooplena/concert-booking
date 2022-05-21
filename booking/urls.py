from . import views
from django.urls import path

urlpatterns = [
    path("index.html", views.ConcertList.as_view(), name="home"),
]