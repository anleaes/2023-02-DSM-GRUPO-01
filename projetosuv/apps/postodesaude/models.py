from django.db import models

# Create your models here.

class PostoDeSaude(models.Model):
    nome = models.CharField('Nome', max_length=50)
    endereco = models.TextField('Endereço', max_length=100)
    horario_funcionamento = models.TimeField('Horário de Funcionamento')

    class Meta:
        verbose_name = 'Posto de Saúde'
        verbose_name_plural = 'Postos de Saúde'
        ordering =['id']

    def __str__(self):
        return self
