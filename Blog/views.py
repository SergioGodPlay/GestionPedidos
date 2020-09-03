from django.shortcuts import render
from Blog.models import Categoria, Post

# Create your views here.
def blogs(request):

    posts = Post.objects.all()
    #categorias = Categoria.objects.all()

    return render(request, "blogs/blog.html", {'posts':posts})