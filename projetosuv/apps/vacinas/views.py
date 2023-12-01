from django.shortcuts import render
from .models import Vacina
from rest_framework import viewsets
from .serializer import VacinaSerializer
# Create your views here.
class VacinaViewSet(viewsets.ModelViewSet):
    queryset = Vacina.objects.all()
    serializer_class = VacinaSerializer