from rest_framework import viewsets, mixins
from rest_framework.permissions import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response

from .models import *
from .serializers import *

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class IngenziViewset(viewsets.ModelViewSet):
    queryset = Ingenzi.objects.filter(is_delete=False)
    permission_classes = IsAuthenticatedOrReadOnly,
    serializer_class = IngenziSerializer

    def destroy(self, request, pk):
        igihanaguwe:Ingenzi = self.get_object()
        igihanaguwe.is_delete = True
        igihanaguwe.save()
        return Response({"inyushu": "vyahanaguwe neza"}, 204)

class UrugendoViewset(viewsets.ModelViewSet):
    queryset = Urugendo.objects.all()
    permission_classes = IsAuthenticatedOrReadOnly, #IsAdminUser
    serializer_class = UrugendoSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = AllowAny, #IsAdminUser
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user:User = serializer.save()
        user.set_password(serializer.data["password"])
        user.save()
        serializer = self.get_serializer(user)

        return Response(serializer.data, 201)

class ItikeViewset(viewsets.ModelViewSet):
    queryset = Itike.objects.filter(ingenzi__is_delete=False)
    permission_classes = IsAuthenticatedOrReadOnly,
    serializer_class = ItikeSerializer

    def perform_create(self, serializer):
        serializer.save(uwayimuhaye=self.request.user)
        return serializer

