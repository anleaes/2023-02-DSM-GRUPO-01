from django.db import models
from lotedevacinas.models import LoteDeVacina
# Create your models here.
class Vacina(models.Model):
    nome = models.CharField(verbose_name='Nome',max_length=50)
    dosepadrao = models.DecimalField(verbose_name='Dose Padrão', max_digits=4, decimal_places=4)
    lotedevacina = models.ForeignKey(LoteDeVacina,verbose_name='Lote de Vacina')
    class Meta:
        verbose_name = 'Vacina'
        verbose_name_plural = 'Vacinas'
        ordering = ['id']

        def __str__(self):
            return self 