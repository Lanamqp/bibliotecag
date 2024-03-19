from django.contrib import admin
from django.urls import include, path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(),name='index'),
    path('livros/', LivrosView.as_view(),name = 'livros'),
    path('leitor/', UsuariosView.as_view(),name = 'leitor'),
    path('autor/', AutoresView.as_view(),name = 'autor'),
    path('cidade/', CidadesView.as_view(),name = 'cidade'),
    path('editora/', EditorasView.as_view(),name = 'editora'),
    path('genero/', GenerosView.as_view(),name = 'genero'),
    path('emprestimo/', EmprestimoView.as_view(),name = 'emprestimo'),

]