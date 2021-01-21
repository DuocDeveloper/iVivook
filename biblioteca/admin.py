from django.contrib import admin
from django.db.models.fields import files
from .models import Autor, Libro, Existencia, Galeria

# Register your models here.
admin.site.register(Galeria)

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre','apellidos', 'nacimiento', 'defuncion')
    fields = ['nombre', 'apellidos', ('nacimiento', 'defuncion')]

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Información', {
            'fields': ('titulo', 'autor', 'categoria')
        }),
        ('Editorial', {
            'fields': ('ISBN', 'editorial', 'año', 'paginas', 'nroEdicion', 'reseña')
        })
    )

@admin.register(Existencia)
class ExistenciaAdmin(admin.ModelAdmin):
    list_filter = ('estado', 'formato')



