

from django.urls import path
from . import views


app_name = 'listing'


urlpatterns = [

    path('', views.Home, name='home'),
    path('about/', views.About, name='about'),
    path('listings/', views.Listings, name='listings'),

]
