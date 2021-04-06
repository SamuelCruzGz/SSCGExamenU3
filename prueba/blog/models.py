from django.db import models

# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=200)
    fecha = models.DateField()
