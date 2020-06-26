from django.db import models
from django.contrib.auth.models import User



from listing.models import Property


# Create your models here.


class Contact(models.Model):

    user_name = models.ForeignKey(User,  related_name='User' ,on_delete=models.CASCADE)
    listing = models.ForeignKey(Property, related_name='Property',  on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("Contacts")

    def __str__(self):
        return self.user_name.username

