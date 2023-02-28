from rest_framework import viewsets, permissions

from .models import Sexo
from .serializers import SexoSerializer

class SexoViewSet(viewsets.ModelViewSet):
    queryset = Sexo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SexoSerializer