from django.contrib import admin
from django.urls import path,include
from login import views

app_name = 'login'

urlpatterns = [
    
   path('', views.home, name='home'),
    path('login/', views.login, name='login'),  # Login URL
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    
    
 
 
]
