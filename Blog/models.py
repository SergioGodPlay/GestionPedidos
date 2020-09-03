from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length = 50)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    #Clase interna Meta para darle un nombre descriptivo al modelo
    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    
    #Funcion __str__ que devuelve el nombre
    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length = 50)
    contenido = models.CharField(max_length = 50)

    #La imagen puede ser opcional
    imagen = models.ImageField(upload_to='blog', null=True, blank = True)
    autor = models.ForeignKey(User, on_delete = models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    #Clase interna Meta para darle un nombre descriptivo al modelo
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
    
    #Funcion __str__ que devuelve el titulo
    def __str__(self):
        return self.titulo