# pojistenci/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_pojisteny, name='add_pojisteny'),
    path('list/', views.list_pojistencu, name='list_pojistencu'),
]
