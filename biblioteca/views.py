from django.shortcuts import render
from django.views import generic
from .models import Libro, Autor, Existencia

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
