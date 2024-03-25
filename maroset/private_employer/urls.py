from django.urls import path, include
from . import views



urlpatterns = [
    path('home', views.private_employer, name='private_home'),
    
]