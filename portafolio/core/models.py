from django.db import models

# Create your models here.


class Contact(models.Model):
    cellphone = models.CharField(max_length=15)
    payment = models.IntegerField()

    def __str__(self):
        return 'Contacto'

