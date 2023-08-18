"""
URL configuration for CVD_UI project.

"""
from django.urls import path

from CVD_UI import views

urlpatterns = [

    # urls accessable to users
    path('', views.home, name='home'),
    path('result/', views.result, name='result'),
]
