from .models import Mensaje, Categoria
from .serializers import CategoriaSerializer, MensajeSerializer
from rest_framework import viewsets, permissions

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CategoriaSerializer

class MensajeViewSet(viewsets.ModelViewSet):
    queryset = Mensaje.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MensajeSerializer