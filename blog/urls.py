from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio),
    path('autor/', crear_autor),
    path('categoria/', crear_categoria),
    path('post/', crear_post),
    path('buscar/', buscar_post),
]