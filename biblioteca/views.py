from django.db import reset_queries
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Libro, Autor, Existencia
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

@login_required
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

class LibroListView(LoginRequiredMixin, ListView):
    model = Libro
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

class LibroDetailView(DetailView):
    model = Libro

class AutorListView(ListView):
    model = Autor

class AutorDetailView(DetailView):
    model = Autor

class AutorCreate(CreateView):
    model = Autor
    fields = ['nombre', 'apellidos', 'nacimiento', 'defuncion']


class AutorUpdate(UpdateView):
    model = Autor
    fields = ['nombre', 'apellidos', 'nacimiento', 'defuncion']

class AutorDelete(DeleteView):
    model = Autor
    success_url = reverse_lazy('autor')




