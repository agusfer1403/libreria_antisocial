from django.db import models

# Create your models here.

class Guitarra(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    numero_cuerdas = models.PositiveIntegerField()

class Bajo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=50)


class Bateria(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    numero_piezas = models.PositiveIntegerField()

class GuitarraElectrica(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    numero_cuerdas = models.PositiveIntegerField()
