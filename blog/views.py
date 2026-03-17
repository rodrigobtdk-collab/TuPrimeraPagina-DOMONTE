from django.shortcuts import render
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaPostForm
from .models import Post

def inicio(request):
    return render(request, "blog/inicio.html")


def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AutorForm()

    return render(request, "blog/form.html", {"form": form})


def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoriaForm()

    return render(request, "blog/form.html", {"form": form})


def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()

    return render(request, "blog/form.html", {"form": form})


def buscar_post(request):
    posts = []

    if request.method == "POST":
        form = BusquedaPostForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data["titulo"]
            posts = Post.objects.filter(titulo__icontains=titulo)
    else:
        form = BusquedaPostForm()

    return render(request, "blog/busqueda.html", {
        "form": form,
        "posts": posts
    })
