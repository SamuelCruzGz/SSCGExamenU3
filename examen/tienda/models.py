from django.db import models

# Create your models here.
class Prendas(models.Model):

    Marca = models.CharField(max_length=50)
    NombrePrenda = models.CharField(max_length=50)
    Categoría = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=200)
    Imagen = models.ImageField(upload_to="media/prenda", default='')
    