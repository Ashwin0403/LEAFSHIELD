from django.contrib import admin
from django.urls import path,include
from diseases import views

app_name = 'diseases'  

urlpatterns = [
    
    path('capture/', views.capture, name='capture'),  # Redirect target
    path('diseases/', views.predict_disease, name='predict_disease'),
    
   #path('capture', views.capture, name='capture'),
    # path('predict/', views.predict_disease, name='predict_disease'),
]
