from django.contrib import admin
from .models import Property, Realtor, Mvp 
from solo.admin import SingletonModelAdmin
# Register your models here.

admin.site.register(Property)
admin.site.register(Realtor)
admin.site.register(Mvp)






