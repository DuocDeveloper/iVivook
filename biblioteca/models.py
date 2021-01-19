from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    apellidos = models.CharField(verbose_name="Apellidos", max_length=100)
    nacimiento = models.DateField(verbose_name="Fecha Nacimiento")
    defuncion = models.DateField(verbose_name="Fecha Defunción", null=True, blank=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellidos
    


'''
Libro
- Titulo
- Autor 
- Editorial
- Año
- Paginas
- ISBN 
- N° Edición
- ReseñaLibro
- Categoría 

Existencia 
- Libro 
- Formato 
- Idioma 
- Estado

Galeria
- Libro
- Estado

Autor 
- Nombre
- Apellidos 
- Año Nacimiento
- Año Defunción 
'''
