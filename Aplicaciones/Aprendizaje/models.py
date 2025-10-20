from django.db import models

# Create your models here.
class Aprendizaje(models.Model):
    edad = models.PositiveIntegerField
    peso = models.FloatField