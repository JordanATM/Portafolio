from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(upload_to='projects', verbose_name='Imagen')
    link = models.URLField(max_length=180, null=True, blank= True)
    created = models.DateTimeField(auto_now_add= True, verbose_name='Fecha Creación')
    updated = models.DateTimeField(auto_now= True, verbose_name= 'Fecha Actualización')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created' ]