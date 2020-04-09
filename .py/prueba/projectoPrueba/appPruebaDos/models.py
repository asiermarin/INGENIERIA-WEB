from django.db import models

class Duracion(models.Model): 
    # Si no se pone ya hay un foreigh key predeterminado de integer
    nombre = models.CharField(max_length = 50)
    duracionMin = models.IntegerField()

class Genero(models.Model):
    nombre = models.CharField(max_length = 50)

class Articulo(models.Model):
    duracion = models.ForeignKey(Duracion, on_delete = models.CASCADE) # Solo tiene una duracion
    genero = models.ManyToManyField(Genero) # Puede tener varios generos
    nombre = models.CharField(max_length = 40)
    fecha_creacion = models.DateField()
    numero_articulo = models.IntegerField()

    def __str__(self):
        return f"id={self.id}, nomnbre={self.nombre}, numero_articulo={self.numero_articulo}"
