from django.contrib import admin

# Register your models here.
from .models import SiteConfiguration
from solo.admin import SingletonModelAdmin
# Register your models here.


admin.site.register(SiteConfiguration, SingletonModelAdmin)