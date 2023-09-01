from rest_framework import viewsets, mixins
from rest_framework.permissions import *
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import *
from .serializers import *

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class IngenziViewset(viewsets.ModelViewSet):
    queryset = Ingenzi.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    serializer_class = IngenziSerializer

class UrugendoViewset(viewsets.ModelViewSet):
    queryset = Urugendo.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly, #IsAdminUser
    serializer_class = UrugendoSerializer

class ItikeViewset(viewsets.ModelViewSet):
    queryset = Itike.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly,
    serializer_class = ItikeSerializer

    def perform_create(self, serializer):
        serializer.save(uwayimuhaye=self.request.user)
        return serializer

