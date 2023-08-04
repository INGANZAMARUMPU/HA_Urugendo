from rest_framework import serializers
from .models import *

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
