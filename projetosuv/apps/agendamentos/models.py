from django.db import models
from pacientes.models import Paciente
from postodesaude.models import PostoDeSaude
# Create your models here.

class Agendamentos(models.Model):
    paciente = models.ForeignKey(Paciente, verbose_name = 'Paciente', on_delete = models.CASCADE )
    postodesaude = models.ForeignKey(PostoDeSaude, verbose_name ='Posto de Saúde', on_delete = models.CASCADE)
    datahora = models.DateTimeField('Data e Hora')

    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        ordering =['id']

    def __str__(self):
        return self