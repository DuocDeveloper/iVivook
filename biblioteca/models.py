from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=50)
    apellidos = models.CharField(verbose_name="Apellidos", max_length=100)
    nacimiento = models.DateField(verbose_name="Fecha Nacimiento")
    defuncion = models.DateField(verbose_name="Fecha Defunción", null=True, blank=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellidos
    
class Libro(models.Model):
    CATEGORIAS = [('1','Romance'),('2','Acción'),('3','Aventura'),('4','Comedia')]
    titulo = models.CharField(verbose_name="Titulo", max_length=250)
    autor = models.ForeignKey(Autor, on_delete=models.DO_NOTHING, verbose_name="Autor")
    editorial = models.CharField(verbose_name="Editorial", max_length=100)
    año = models.IntegerField(verbose_name="Año")
    paginas = models.IntegerField(verbose_name="Paginas")
    ISBN = models.CharField(verbose_name="ISBN", max_length=20)
    nroEdicion = models.IntegerField(verbose_name="N° Edición")
    reseña = models.TextField(verbose_name="Reseña")
    categoria = models.CharField(verbose_name="Categoría", choices=CATEGORIAS, max_length=1)

    def __str__(self):
        return self.titulo

class Existencia(models.Model): 
    FORMATOS = [('D','Digital'),('F', 'Fisico')]
    ESTADOS = [('D', 'Disponible'), ('P', 'Prestamo'), ('M', 'Mantención')]
    libro = models.ForeignKey(Libro, verbose_name="Libro", on_delete=models.DO_NOTHING) 
    formato = models.CharField(verbose_name="Formato", choices=FORMATOS, max_length=1) 
    idioma = models.CharField(verbose_name="Idioma", max_length=50)
    estado = models.CharField(verbose_name="Estado", choices=ESTADOS, max_length=1) 
    entrega = models.DateField(verbose_name="Fecha Entrega", null=True, blank=True)
    devolucion = models.DateField(verbose_name="Fecha Devolución", null=True, blank=True)

class Galeria(models.Model):
    libro = models.ForeignKey(Libro, verbose_name="Libro", on_delete=models.DO_NOTHING) 
    imagen = models.FileField(upload_to='images/', verbose_name='Imagen')
    estado = models.BooleanField(verbose_name='Estado')

