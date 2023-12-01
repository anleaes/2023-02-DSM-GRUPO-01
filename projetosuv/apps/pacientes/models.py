from django.db import models

# Create your models here.

class Pacientes(models.Model):
    nome = models.CharField('Nome', max_length=50)
    data_de_nascimento = models.DateField('Data de Nascimento', max_length=100)
