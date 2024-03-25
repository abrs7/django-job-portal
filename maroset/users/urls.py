from django.urls import path
from . import views



urlpatterns = [
   path('register-candidate/', views.register_candidate, name='register-candidate'),
   path('register-company/', views.register_company, name='register-company'),
   path('register-private/', views.register_private_recruiter, name='register-private'),
   path('login', views.login_user, name='login'),
   path('logout', views.logout_user, name='logout'),
   

    
]