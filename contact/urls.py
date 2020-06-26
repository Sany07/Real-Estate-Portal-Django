

from django.urls import path
from .views import ContactView


app_name = "contactapp"

urlpatterns = [


    path('', ContactView.as_view(), name='contact'),



]
