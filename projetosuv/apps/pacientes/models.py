from django.db import models

# Create your models here.

class Paciente(models.Model):
    nome = models.CharField('Nome', max_length=50)
    data_de_nascimento = models.DateField('Data de Nascimento')
    endereco = models.TextField('Endereço', max_length=200)
    telefone = models.CharField('Telefone')

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering =['id']

    def __str__(self):
        return self
