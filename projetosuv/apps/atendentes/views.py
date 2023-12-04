from .models import Atendente
from rest_framework import viewsets
from .serializer import AtendenteSerializer

class AtendenteViewSet(viewsets.ModelViewSet):
    queryset = Atendente.objects.all()
    serializer_class = AtendenteSerializer