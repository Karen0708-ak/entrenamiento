from django.urls import path
from . import views

urlpatterns = [
    path('', views.predecir_peso, name='predecir_peso'),
]
