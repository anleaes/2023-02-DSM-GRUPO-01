from django.db import models
from postodesaude.models import PostoDeSaude
# Create your models here.
class Especialidade(models.Model):
    nome = models.CharField('Nome', max_length=50)
    especialidade = models.CharField('Especialidade', max_length=50)
    