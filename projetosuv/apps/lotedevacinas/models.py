from django.db import models

# Create your models here.
class LoteDeVacina(models.Model):
    fabricante = models.CharField('Fabricante', max_length=50)
    data_de_fabricacao = models.DateField('Data de Fabricação')
    quantidade =  models.IntegerField('Quantidade')
    data_de_validade = models.DateField('Data de Validade')
    
    class Meta:
        verbose_name = 'Lote de Vacina'
        verbose_name_plural = 'Lote de Vacinas'
        ordering =['id']

    def __str__(self):
        return f"{self.fabricante} - {self.data_de_validade}"
