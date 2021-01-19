from django.contrib import admin
from .models import Autor, Libro, Existencia, Galeria

# Register your models here.
admin.site.register(Autor)
admin.site.register(Libro)
admin.site.register(Existencia)
admin.site.register(Galeria)
