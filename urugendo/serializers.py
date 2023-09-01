from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, instance):
        data = super().validate(instance)
        data["izina"] = self.user.username
        data["is_superuser"] = self.user.is_superuser
        data["amagroupes"] = [ group.name for group in self.user.groups.all() ]
        return data

class IngenziSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingenzi
        fields = "__all__"
   
class UrugendoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Urugendo
        fields = "__all__"
    
class ItikeSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["ingenzi"] = instance.ingenzi.izina
        return data

    class Meta:
        model = Itike
        fields = "__all__"
        read_only_fields = "uwayimuhaye",


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField()

    class Meta:
        model = User
        exclude = "groups", "user_permissions", "date_joined", "last_login"
        read_only_fields = "is_superuser", "is_staff", 'is_active'