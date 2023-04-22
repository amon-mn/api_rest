from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_users, name='get_all_users'),
    path('user/<str:login>', views.get_by_login),
    path('data/', views.user_manager)
]