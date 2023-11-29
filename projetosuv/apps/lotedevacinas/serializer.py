from .models import LoteDeVacina
from rest_framework import serializers

class LoteDeVacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoteDeVacina
        fields = '__all__'