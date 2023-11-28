from django.shortcuts import render
from .models import LoteDeVacina
from rest_framework import viewsets
from .serializer import LoteDeVacinaSerializer
# Create your views here.
class LoteDeVacinasViewSet(viewsets.ModelViewSet):
    queryset = LoteDeVacina.objects.all()
    serializer_class = LoteDeVacinaSerializer  