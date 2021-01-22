from os import name
from django.urls import path, re_path
from . import views
from . import form


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^libros/$', views.LibroListView.as_view(), name='libros'),
    re_path(r'^libros/(?P<pk>\d)$', views.LibroDetailView.as_view(), name='libro-detail'),
    re_path(r'^autor/$', views.AutorListView.as_view(), name='autor'),
    re_path(r'^autor/(?P<pk>\d)$', views.AutorDetailView.as_view(), name='autor_detail'),
    re_path(r'^autor/create/$', views.AutorCreate.as_view(), name='autor_create'),
    re_path(r'^autor/(?P<pk>\d+)/update$', views.AutorUpdate.as_view(), name='autor_update'),
    re_path(r'^autor/(?P<pk>\d+)/delete$', views.AutorDelete.as_view(), name='autor_delete'),
]


