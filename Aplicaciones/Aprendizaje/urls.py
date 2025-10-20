from django.urls import path
from . import views

urlpatterns = [
    path('aprend', views.inicio, name='aprend'),
]
