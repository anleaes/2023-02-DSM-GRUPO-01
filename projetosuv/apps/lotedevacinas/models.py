from dataclasses import dataclass
from msilib.schema import Class
from django.db import models

# Create your models here.
class Category(models.Model):
    fabricante = models.CharField('Fabricante', max_length=50)
    data_de_fabricacao = models.DateField('Data de Fabricação', max_length=100)
    
    class Meta:
        verbose_name = 'Lote de Vacina'
        verbose_name_plural = 'Lote de Vacinas'
        ordering =['id']

    def __str__(self):
        return self