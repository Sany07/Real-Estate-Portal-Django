from django.db import models
from solo.models import SingletonModel
# Create your models here.


class SiteConfiguration(SingletonModel):
    site_name = models.CharField(max_length=50, default='YourSiteName')
    phone = models.CharField(max_length=20,default='YourPhoneNumber')
    email = models.EmailField(max_length=50,default='YourEmailName')

    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"