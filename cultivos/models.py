from django.db import models

class Cultivo(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()
    siembra = models.CharField(max_length=100)
    cosecha = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre