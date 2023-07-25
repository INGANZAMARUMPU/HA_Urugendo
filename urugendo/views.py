from rest_framework import viewsets

from .models import *
from .serializers import *

class IngenziViewset(viewsets.ModelViewSet):
    queryset = Ingenzi.objects.all()
    serializer_class = IngenziSerializer

class UrugendoViewset(viewsets.ModelViewSet):
    queryset = Urugendo.objects.all()
    serializer_class = UrugendoSerializer

class ItikeViewset(viewsets.ModelViewSet):
    queryset = Itike.objects.all()
    serializer_class = ItikeSerializer

    def perform_create(self, serializer):
        serializer.save(uwayimuhaye=self.request.user)
        return serializer

