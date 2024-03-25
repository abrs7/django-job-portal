from django.urls import path
from . import views



urlpatterns = [
   path('home', views.company_regsiter, name='company_profile'),
    
]