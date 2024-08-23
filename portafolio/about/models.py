from django.db import models

# Create your models here.
#Modelo para formación = Course

class Course(models.Model):
    title = models.CharField(max_length=150, verbose_name= 'Titulo')
    degree_title =  models.CharField(max_length=300, verbose_name= 'Titulo obtenido')
    description = models.TextField(verbose_name= 'Descripción')
    created = models.DateTimeField(auto_now_add=True,verbose_name= 'Fecha creación')
    updated = models.DateTimeField(auto_now= True, verbose_name= 'Fecha actualización')

    class Meta:
        verbose_name = 'Formación'
        verbose_name_plural = 'Formaciones'
        ordering = ['-created']

    def __str__(self):
        return self.title

 
#Modelo para Skills
class Skill(models.Model):
   title = models.CharField(max_length=80, verbose_name= 'Titulo')
   image = models.ImageField(upload_to='skills', verbose_name='Imagen')
   created = models.DateTimeField(auto_now_add=True,verbose_name= 'Fecha creación')
   updated = models.DateTimeField(auto_now= True, verbose_name= 'Fecha actualización')

   class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'
        ordering = ['-created']

   def __str__(self):
        return self.title