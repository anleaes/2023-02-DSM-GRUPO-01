from django.db import models

# Create your models here.

class PostoDeSaude(models.Model):
    nome = models.CharField('Nome', max_length=50)
    endereco = models.TextField('Endereço', max_length=100)
    horario_funcionamento = models.TimeField('Horário de Funcionamento')
