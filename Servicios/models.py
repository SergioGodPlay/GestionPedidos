from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length = 50)
    contenido = models.CharField(max_length = 50)
    imagen = models.ImageField(upload_to='servicios')
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    #Clase interna Meta para darle un nombre descriptivo al modelo
    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
    
    #Funcion __str__ que devuelve el titulo
    def __str__(self):
        return self.titulo