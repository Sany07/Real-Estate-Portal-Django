from django.db import models
from django.urls import reverse
from solo.models import SingletonModel


# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/realtor/%Y-%m-%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    hire_date = models.DateTimeField(auto_now_add=True, blank=True)
  


    class Meta:
        verbose_name = "Realtor"
        verbose_name_plural = "Realtors"

    def __str__(self):
        return self.name

class Mvp(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)    

    class Meta:
        verbose_name = "MVP"
        verbose_name_plural = "MVP"

    def __str__(self):
        return self.realtor.name 

    

class Property(models.Model):

    realtor = models.ForeignKey(Realtor, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    thumb_nail = models.ImageField(upload_to='photos/listings/%Y-%m-%d/')
    photo_1 = models.ImageField(upload_to='photos/listings/%Y-%m-%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/listings/%Y-%m-%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/listings/%Y-%m-%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/listings/%Y-%m-%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/listings/%Y-%m-%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/listings/%Y-%m-%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("listing:listing-detail", kwargs={"id": self.id})



