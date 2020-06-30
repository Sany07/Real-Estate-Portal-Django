

from django.urls import include, path
from .views import RegisterView, LoginView, dashboard, LogoutView , DashBoardView


app_name = "account"

urlpatterns = [


    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', DashBoardView.as_view(), name='dashboard'),
    



]
