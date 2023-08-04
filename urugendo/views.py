from rest_framework import viewsets, mixins
from rest_framework.permissions import *

from .models import *
from .serializers import *

class IngenziViewset(viewsets.ModelViewSet):
    queryset = Ingenzi.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
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

