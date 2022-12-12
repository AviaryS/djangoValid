from django.urls import path
from engine import views

urlpatterns = [
    path('reg/', views.register, name='register'),
    path('log/', views.login, name='login'),
]
