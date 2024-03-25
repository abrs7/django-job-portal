from django.urls import path
from . import views



urlpatterns = [
   path('candidates/', views.candidate_home, name='candidate_profile'),

    
]