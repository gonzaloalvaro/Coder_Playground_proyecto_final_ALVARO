from django.db import models

# Create your models here.

class ropa(models.Model):
    nombre = models.CharField(max_length=50)
    prenda = models.TextField()
    descripcion = models.TextField()
    talle = models.TextField()
    cantidad_en_stock = models.IntegerField()
    def __str__(self):
        return self.nombre + " - " + self.descripcion

class accesorios(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.TextField()
    descripcion = models.TextField()
    talle = models.TextField()
    cantidad_en_stock = models.IntegerField()

    def __str__(self):
        return self.nombre + " - " + self.descripcion

class anteojos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    color = models.TextField()
    cantidad_en_stock = models.IntegerField()

    def __str__(self):
        return self.nombre + " - " + self.descripcion