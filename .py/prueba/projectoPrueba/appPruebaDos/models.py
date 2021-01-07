from django.db import models

class Duracion(models.Model): 
    # Si no se pone ya hay un foreigh key predeterminado de integer
    nombre = models.CharField(max_length = 50)
    duracionMin = models.IntegerField()

    def __str__(self):
        return f"nombre = {self.genero}"

class Genero(models.Model):
    nombre = models.CharField(max_length = 50)

    def __str__(self):
        return f"id={self.id}, nombre = {self.nombre}"

class Articulo(models.Model):
    duracion = models.ForeignKey(Duracion, on_delete = models.CASCADE) # Solo tiene una duracion
    genero = models.ManyToManyField(Genero) # Puede tener varios generos
    nombre = models.CharField(max_length = 40)
    fecha_creacion = models.DateField()
    numero_articulo = models.IntegerField()
    # un_numero = models.IntegerField()w

    def __str__(self):
        return f"id={self.id}, nomnbre={self.nombre}, numero_articulo={self.numero_articulo}, duracion = {self.duracion.nombre}, generos = {' / '.join(genero.nombre for genero in self.genero.all())}"
