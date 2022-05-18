from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=130)
    venue_image = CloudinaryField('image', default='placeholder')
    address = models.CharField(max_length=290)
    zip_code = models.CharField('Zip Code', max_length=20)
    email = models.EmailField('Email')
    phone_number = models.CharField('Phone Number', max_length=30)

    def __str__(self):
        return self.name


class Concert(models.Model):
    concert_date = models.DateTimeField('Concert Date')
    name = models.CharField('Concert Name', max_length=130)
    venue = models.ForeignKey(Venue, blank=True, on_delete=models.CASCADE)
    concert_information = models.TextField(blank=True)
    concert_image = CloudinaryField('image', default='placeholder')
    concert_goers = models.ManyToManyField(User, blank=True)
    concert_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["concert_created"]

    def __str__(self):
        return self.name

