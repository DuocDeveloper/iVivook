from django.db import reset_queries
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from .models import Libro, Autor, Existencia
from django.urls import reverse_lazy

# Create your views here.


def index(request):
    libros = Libro.objects.all().count()
    existencias = Existencia.objects.all().count()
    disponibles = Existencia.objects.filter(estado='D').count()
    autores = Autor.objects.all().count()

    return render(
        request,
        'index.html',
        context={'libros': libros, 'existencias': existencias,
                 'autores': autores, 'disponibles': disponibles}
    )

class LibroListView(generic.ListView):
    model = Libro

class LibroDetailView(generic.DetailView):
    model = Libro

class AutorListView(generic.ListView):
    model = Autor

class AutorDetailView(generic.DetailView):
    model = Autor

class AutorCreate(generic.edit.CreateView):
    model = Autor
    fields = ['nombre', 'apellidos', 'nacimiento', 'defuncion']


class AutorUpdate(generic.edit.UpdateView):
    model = Autor
    fields = ['nombre', 'apellidos', 'nacimiento', 'defuncion']

class AutorDelete(generic.edit.DeleteView):
    model = Autor
    success_url = reverse_lazy('autor')




