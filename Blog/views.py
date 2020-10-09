from django.shortcuts import render
from Blog.models import Categoria, Post

# Create your views here.
def blogs(request):

    posts = Post.objects.all()
    #categorias = Categoria.objects.all()

    return render(request, "blogs/blog.html", {'posts':posts})


def categorias(request, categoria_id):

    categoria = Categoria.objects.get(id = categoria_id)

    posts = Post.objects.filter(categorias = categoria)

    return render(request, "blogs/categorias.html", {'categoria':categoria, 'posts':posts})