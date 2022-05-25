from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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
    total_left = models.IntegerField(default=50)
    

    def __str__(self):
        return self.name

  
    
class Ticket(models.Model):
    concert = models.ForeignKey(Concert, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    order = models.IntegerField(default=0)
    

    def __str__(self):
        return self.user.username
    
    
    

        
             

    
