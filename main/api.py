from .models import Conc
from rest_framework import viewsets, permissions
from .serializers import ConcSerializer

class ConcViewSet(viewsets.ModelViewSet):
    queryset = Conc.objects.all()
    permissions_classes =[
        permissions.AllowAny
    ]
    serializer_class = ConcSerializer