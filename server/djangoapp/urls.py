from django.urls import path
from . import views

urlpatterns = [
    path('get_cars', views.get_cars, name='getcars'),
]